from __future__ import absolute_import

from ..version_info import PY3

if PY3:
    from urllib.parse import *
else:
    from robotparser import *
