from __future__ import absolute_import

import sys
from functools import *

from .version_info import PY2, PY3

if PY2:
    reduce = reduce

if sys.version_info <= (3, 2):
    from .collections import namedtuple
    try:
        from threading import RLock
    except ImportError:
        from dummy_threading import RLock

    if PY3:
        integer_types = (int, )
    else:
        integer_types = (int, long)

    _CacheInfo = namedtuple("CacheInfo", ["hits", "misses", "maxsize", "currsize"])

    class _HashedSeq(list):
        """ This class guarantees that hash() will be called no more than once
            per element.  This is important because the lru_cache() will hash
            the key multiple times on a cache miss.

        """

        __slots__ = 'hashvalue'

        def __init__(self, tup, hash=hash):
            self[:] = tup
            self.hashvalue = hash(tup)

        def __hash__(self):
            return self.hashvalue

    def _make_key(args, kwds, typed,
                  kwd_mark=(object(),),
                  fasttypes=set([int, str, frozenset, type(None)]),
                  sorted=sorted, tuple=tuple, type=type, len=len):
        """Make a cache key from optionally typed positional and keyword arguments

        The key is constructed in a way that is flat as possible rather than
        as a nested structure that would take more memory.

        If there is only a single argument and its data type is known to cache
        its hash value, then that argument is returned without a wrapper.  This
        saves space and improves lookup speed.

        """
        key = args
        if kwds:
            sorted_items = sorted(kwds.items())
            key += kwd_mark
            for item in sorted_items:
                key += item
        if typed:
            key += tuple(type(v) for v in args)
            if kwds:
                key += tuple(type(v) for k, v in sorted_items)
        elif len(key) == 1 and type(key[0]) in fasttypes:
            return key[0]
        return _HashedSeq(key)

    def lru_cache(maxsize=128, typed=False):
        """Least-recently-used cache decorator.

        If *maxsize* is set to None, the LRU features are disabled and the cache
        can grow without bound.

        If *typed* is True, arguments of different types will be cached separately.
        For example, f(3.0) and f(3) will be treated as distinct calls with
        distinct results.

        Arguments to the cached function must be hashable.

        View the cache statistics named tuple (hits, misses, maxsize, currsize)
        with f.cache_info().  Clear the cache and statistics with f.cache_clear().
        Access the underlying function with f.__wrapped__.

        See:  http://en.wikipedia.org/wiki/Cache_algorithms#Least_Recently_Used

        """

        # Users should only access the lru_cache through its public API:
        #       cache_info, cache_clear, and f.__wrapped__
        # The internals of the lru_cache are encapsulated for thread safety and
        # to allow the implementation to change (including a possible C version).

        # Early detection of an erroneous call to @lru_cache without any arguments
        # resulting in the inner function being passed to maxsize instead of an
        # integer or None.
        if maxsize is not None and not isinstance(maxsize, integer_types):
            raise TypeError('Expected maxsize to be an integer or None')

        def decorating_function(user_function):

            cache = dict()
            stats = [0, 0]                  # make statistics updateable non-locally
            HITS, MISSES = 0, 1             # names for the stats fields
            make_key = _make_key            # build a key from the function arguments
            cache_get = cache.get           # bound method to lookup key or return None
            _len = len                      # localize the global len() function
            lock = RLock()                  # because linkedlist updates aren't threadsafe
            root = []                       # root of the circular doubly linked list
            root[:] = [root, root, None, None]      # initialize by pointing to self
            nonlocal_root = [root]                  # make updateable non-locally
            PREV, NEXT, KEY, RESULT = 0, 1, 2, 3    # names for the link fields

            if maxsize == 0:

                def wrapper(*args, **kwds):
                    # No caching -- just a statistics update after a successful call
                    result = user_function(*args, **kwds)
                    stats[MISSES] += 1
                    return result

            elif maxsize is None:

                def wrapper(*args, **kwds):
                    # Simple caching without ordering or size limit
                    key = make_key(args, kwds, typed)
                    result = cache_get(key, root)
                    if result is not root:
                        stats[HITS] += 1
                        return result
                    result = user_function(*args, **kwds)
                    cache[key] = result
                    stats[MISSES] += 1
                    return result

            else:

                def wrapper(*args, **kwds):
                    # Size limited caching that tracks accesses by recency
                    key = make_key(args, kwds, typed) if kwds or typed else args
                    with lock:
                        link = cache_get(key)
                        if link is not None:
                            # Move the link to the front of the circular queue
                            root, = nonlocal_root
                            link_prev, link_next, key, result = link
                            link_prev[NEXT] = link_next
                            link_next[PREV] = link_prev
                            last = root[PREV]
                            last[NEXT] = root[PREV] = link
                            link[PREV] = last
                            link[NEXT] = root
                            stats[HITS] += 1
                            return result
                    result = user_function(*args, **kwds)
                    with lock:
                        root, = nonlocal_root
                        if key in cache:
                            # Getting here means that this same key was added to the
                            # cache while the lock was released.  Since the link
                            # update is already done, we need only return the
                            # computed result and update the count of misses.
                            pass
                        elif _len(cache) >= maxsize:
                            # Use the old root to store the new key and result.
                            oldroot = root
                            oldroot[KEY] = key
                            oldroot[RESULT] = result
                            # Empty the oldest link and make it the new root.
                            # Keep a reference to the old key and old result to
                            # prevent their ref counts from going to zero during the
                            # update. That will prevent potentially arbitrary object
                            # clean-up code (i.e. __del__) from running while we're
                            # still adjusting the links.
                            root = nonlocal_root[0] = oldroot[NEXT]
                            oldkey = root[KEY]
                            root[KEY] = root[RESULT] = None
                            # Now update the cache dictionary.
                            del cache[oldkey]
                            # Save the potentially reentrant cache[key] assignment
                            # for last, after the root and links have been put in
                            # a consistent state.
                            cache[key] = oldroot
                        else:
                            # Put result in a new link at the front of the queue.
                            last = root[PREV]
                            link = [last, root, key, result]
                            last[NEXT] = root[PREV] = cache[key] = link
                        stats[MISSES] += 1
                    return result

            def cache_info():
                """Report cache statistics"""
                with lock:
                    return _CacheInfo(stats[HITS], stats[MISSES], maxsize, len(cache))

            def cache_clear():
                """Clear the cache and cache statistics"""
                with lock:
                    cache.clear()
                    root = nonlocal_root[0]
                    root[:] = [root, root, None, None]
                    stats[:] = [0, 0]

            wrapper.__wrapped__ = user_function
            wrapper.cache_info = cache_info
            wrapper.cache_clear = cache_clear
            return update_wrapper(wrapper, user_function)

        return decorating_function()
