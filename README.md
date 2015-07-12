![Pies](https://raw.github.com/timothycrosley/pies/develop/logo.png)
====================
[![PyPI version](https://badge.fury.io/py/pies.png)](http://badge.fury.io/py/pies)
[![PyPi downloads](https://pypip.in/d/pies/badge.png)](https://crate.io/packages/pies/)
[![Build Status](https://travis-ci.org/timothycrosley/pies.png?branch=develop)](https://travis-ci.org/timothycrosley/pies)
[![License](https://pypip.in/license/pies/badge.png)](https://pypi.python.org/pypi/pies/)
[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/timothycrosley/pies/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

The simplest (and tastiest) way to write one program that runs on both Python 2.6+ and Python 3.

Let's eat some pies!
======================

Installing pies

    pip install pies

or if you prefer:

    easy_install pies

Overview
====================

Pies is a Python2 & 3 Compatibility layer with the philosophy that all code should be Python3 code.
Starting from this viewpoint means that when running on Python3 pies adds virtually no overhead.

Instead of providing a bunch of custom methods (leading to Python code that looks out of place on any version)
pies aims to back port as many of the Python3 api calls, imports, and objects to Python2 - Relying on special syntax
only when absolutely necessary.

How does pies differ from six?
====================

Pies is significantly smaller and simpler than six because it assumes for
everything possible the developer is using the Python 3 compatible versions included with Python 2.6+,
whereas six tries to maintain compatibility with Python 2.4 -
leading to many more overrides and further into different language territory.
Additionally, as stated above, where possible pies tries to enable you to not have to change syntax at all.

Integrating pies into your diet
======================

Using and integrating pies into an existing Python 3+ code base (to achieve Python 2 & 3 dual support) couldn't be simpler:

    from __future__ import absolute_import, division, print_function, unicode_literals

    from pies.overrides import *

Then simply write standard Python3 code, and enjoy Python2 Support.

Works Unchanged (The Good)
======================

The best part of Pies is how much Python3 code works unchanged in Python2

Functions:

- round
- next
- filter
- map
- zip
- input
- range

Types:

- object (__str__ automatically has correct behavior on all versions of Python)
- chr (creates a unichr object in Python2)
- str (creates a unicode object in Python2)
- dict (creating a dict using dict() will give you all the special Python3 itemview results, but using {} will not)

Imports:

- html
- http
- xmlrpc
- _thread
- builtins
- configparser
- copyreg
- queue
- reprlib
- socketserver
- ipaddress
- argparse
- enum (also adds this library to Python 3.0-3.3)

Different Imports (The Bad)
======================

Some Python3 Modules have moved around so much compared to their Python2 counterpart, that I found it necessary to create special
versions of them to obtain the Python3 naming on both environments. Since these modules exist already in Python2
allowing them to be imported by the Python3 module name directly is not possible. Instead, you must import these
modules from pies.

Example:

    from pies import pickle

Full List:

- dbm
- urllib
- collections
- functools
- imp
- itertools
- pickle
- StringIO
- sys
- unittest

Special Syntax (The Ugly)
======================

Sadly, there is still special syntax that is present for corner cases.

- PY2 - True if running on Python2
- PY3 - True if running on Python3
- u('text') - should replace u'text' made available for ease of porting code from Python2
- itemsview(collection) - should replace collection.iteritems() where you do not control the collection passed in
- valuesview(collection) - should replace collection.values() where you do not control the collection passed in
- keysview(collection) - should replace collection.keys() where you do not control the collection passed in
- execute() - enables Python 3 style exec statements on both environments.
- integer_types - may want to use isinstance(variable, integer_types) instead of type(variable, int) as long values will not match int in Python2.
- NewClass(with_metaclass(metaclass, parent_class)) - Should replace both "__metaclass__ = metaclass" and "NewClass(metaclass=metaclass)" as a way to assign meta-classes.

What Could be Improved?
======================

I'm pretty sure a bunch. If you run into any problems or have any ideas please don't hesitate to file a bug, submit a pull request,
or email me at timothy.crosley@gmail.com.

--------------------------------------------

Thanks and I hope you enjoy pies!

~Timothy Crosley
