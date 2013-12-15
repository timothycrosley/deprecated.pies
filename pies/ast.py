from __future__ import absolute_import

from ast import *

from .version_info import PY2

if PY2:
    Try = TryExcept
else:
    TryFinally = ()
