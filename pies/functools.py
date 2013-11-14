from __future__ import absolute_import

from functools import *

from .version_info import PY2

if PY2:
    reduce = reduce
