"""
    pies/overrides.py

    Overrides Python syntax to conform to the Python3 version as much as possible using a '*' import

    Copyright (C) 2013  Timothy Edmund Crosley

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
    documentation files (the "Software"), to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
    to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or
    substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
    TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
    CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.
"""
from __future__ import absolute_import

import functools
from numbers import Integral

from .version_info import PY2, PY3, VERSION

__version__ = "2.0.0"

native_dict = dict
native_round = round
native_filter = filter
native_map = map
native_zip = zip
native_range = range
native_str = str
native_chr = chr
native_input = input
native_next = next

common = ['native_dict', 'native_round', 'native_filter', 'native_map', 'native_range', 'native_str', 'native_chr',
          'native_input', 'PY2', 'PY3', 'u', 'itemsview', 'valuesview', 'keysview', 'execute', 'integer_types',
          'native_next']

if PY3:
    import urllib
    import builtins
    from urllib import parse

    from collections import OrderedDict

    integer_types = (int, )

    def u(string):
        return string

    def itemsview(collection):
        return collection.items()

    def valuesview(collection):
        return collection.values()

    def keysview(collection):
        return collection.keys()

    urllib.quote = parse.quote
    urllib.quote_plus = parse.quote_plus
    urllib.unquote = parse.unquote
    urllib.unquote_plus = parse.unquote_plus
    urllib.urlencode = parse.urlencode
    execute = getattr(builtins, 'exec')
    if VERSION[1] < 2:
        def callable(entity):
            return hasattr(entity, '__call__')
        common.append('callable')

    __all__ = common + ['OrderedDict', 'urllib']
else:
    from itertools import ifilter as filter
    from itertools import imap as map
    from itertools import izip as zip
    from decimal import Decimal, ROUND_HALF_EVEN


    try:
        from collections import OrderedDict
    except ImportError:
        from ordereddict import OrderedDict

    import codecs
    str = unicode
    chr = unichr
    input = raw_input
    range = xrange
    integer_types = (int, long)

    for removed in ('apply', 'cmp', 'coerce', 'execfile', 'raw_input', 'unpacks'):
        def _not_allow(*args, **kwargs):
            raise NameError("name '{0}' is not defined".format(removed))

        _not_allow.__name__ = removed
        globals()[removed] = _not_allow

    def u(string):
        return codecs.unicode_escape_decode(string[0])

    def execute(_code_, _globs_=None, _locs_=None):
        """Execute code in a namespace."""
        if _globs_ is None:
            frame = sys._getframe(1)
            _globs_ = frame.f_globals
            if _locs_ is None:
                _locs_ = frame.f_locals
            del frame
        elif _locs_ is None:
            _locs_ = _globs_
        exec("""exec _code_ in _globs_, _locs_""")

    class _dict_view_base(object):
        __slots__ = ('_dictionary', )

        def __init__(self, dictionary):
            self._dictionary = dictionary

        def __repr__(self):
            return "{0}({1})".format(self.__class__.__name__, str(list(self.__iter__())))

        def __unicode__(self):
            return str(self.__repr__())

        def __str__(self):
            return str(self.__unicode__())

    class dict_keys(_dict_view_base):
        __slots__ = ()

        def __iter__(self):
            return self._dictionary.iterkeys()

    class dict_values(_dict_view_base):
        __slots__ = ()

        def __iter__(self):
            return self._dictionary.itervalues()

    class dict_items(_dict_view_base):
        __slots__ = ()

        def __iter__(self):
            return self._dictionary.iteritems()

    def itemsview(collection):
        return dict_items(collection)

    def valuesview(collection):
        return dict_values(collection)

    def keysview(collection):
        return dict_keys(collection)

    class dict(native_dict):
        def has_key(self, *args, **kwargs):
            return AttributeError("'dict' object has no attribute 'has_key'")

        def items(self):
            return dict_items(self)

        def keys(self):
            return dict_keys(self)

        def values(self):
            return dict_values(self)

    def round(number, ndigits=None):
        return_int = False
        if ndigits is None:
            return_int = True
            ndigits = 0
        if hasattr(number, '__round__'):
            return number.__round__(ndigits)

        if ndigits < 0:
            raise NotImplementedError('negative ndigits not supported yet')
        exponent = Decimal('10') ** (-ndigits)
        d = Decimal.from_float(number).quantize(exponent,
                                                rounding=ROUND_HALF_EVEN)
        if return_int:
            return int(d)
        else:
            return float(d)

    def next(iterator):
        try:
            iterator.__next__()
        except Exception:
            native_next(iterator)

    __all__ = common + ['round', 'dict', 'apply', 'cmp', 'coerce', 'execfile', 'raw_input', 'unpacks', 'str', 'chr',
                        'input', 'range', 'filter', 'map', 'zip']
