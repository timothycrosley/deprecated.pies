pies!
====================

The simplest (and tastiest) way to write one program that runs on both Python 2.6+ and Python 3.


How does pies differ from six?
====================

Pies is significantly smaller and simpler then six because it assumes for
everything possible the developer is using the Python 3 compatible versions included with Python 2.6+,
whereas six tries to maintain compatibility with Python 2.4 -
leading to many more overrides and further into different language territory.
Additionally where possible pies tries to enable you to not have to change syntax at all -
pass including the import.


Let's eat some pies!
======================

Installing pies

    pip install pies

or if you prefer:

    easy_install pies


Integrating pies into your diet
======================

Using and integrating pies into an existing Python 2.6 code base (to achieve Python 3 dual support) couldn't be simpler:

    from pies import *

You will then simply have to make some simple changes to your Python code:

- u'string' -> u('string')
- my_iterable.iteritems -> iteritems(my_iterable)
- my_iterable.itervalues -> itervalues(my_iterable)
- my_iterable.iterkeys -> iterkeys(my_iterable)

The following will work unchanged in Python 3 after import (using the Python 2 syntax):

- xrange
- long
- unicode
- urllib.quote
- urllib.quote_plus
- urllib.unquote
- urllib.unquote_plus
- urllib.urlencode

pies will also automatically install and include the most optimal version of OrderedDict for the Python environment
in use, so you should remove any other explicit imports of OrderedDict.
