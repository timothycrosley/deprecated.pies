from __future__ import absolute_import

from urllib import *

from ..version_info import PY2

if PY2:
    from . import error, parse, request, robotparser
