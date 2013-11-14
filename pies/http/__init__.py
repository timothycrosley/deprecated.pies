from __future__ import absolute_import

from http import *

from ..version_info import PY2

if PY2:
    from . import client, cookiejar, cookies, server
