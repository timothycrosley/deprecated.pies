from __future__ import absolute_import

from dbm import *

from ..version_info import PY2

if PY2:
    from . import dumb, gnu, ndbm
    from whichdb import *
    from anydbm import *
