from __future__ import absolute_import

from ..version_info import PY3

if PY3:
    from urllib.error import *
else:
    from urllib import ContentTooShortError
    from urllib2 import HTTPError, URLError
