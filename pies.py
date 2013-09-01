"""
    pies.py

    Adds necessary hooks to allow Python code to run on multiple major versions of Python at once
    (currently 2.6 - 3.x)

    Usage:
        Anywhere you want to gain support for multiple versions of Python simply add the following line
            from pies import *

    Copyright (C) 2013  Timothy Edmund Crosley

    This program is free software; you can redistribute it and/or
    modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation; either version 2
    of the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

import sys

__version__ = "1.0.0"

if sys.version > '3':
    import urllib
    from urllib import parse

    from collections import OrderedDict

    long = int
    unicode = str

    def u(string):
        return string

    def iteritems(collection):
        return collection.items()

    def itervalues(collection):
        return collection.values()

    def iterkeys(collection):
        return collection.keys()

    def xrange(*args):
        return range(*args)

    urllib.quote = parse.quote
    urllib.quote_plus = parse.quote_plus
    urllib.unquote = parse.unquote
    urllib.unquote_plus = parse.unquote_plus
    urllib.urlencode = parse.urlencode
else:
    try:
        from collections import OrderedDict
    except ImportError:
        from ordereddict import OrderedDict

    import codecs

    def u(string):
        return codecs.unicode_escape_decode(string)[0]

    def iteritems(collection):
        return collection.iteritems()

    def itervalues(collection):
        return collection.itervalues()

    def iterkeys(collection):
        return collection.iterkeys()
