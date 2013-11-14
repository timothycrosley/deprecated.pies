from __future__ import absolute_import

from ..version_info import PY3

if PY3:
    from urllib.parse import *
else:
    from urllib import quote, unquote, quote_plus, unquote_plus, urlencode
