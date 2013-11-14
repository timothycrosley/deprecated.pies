from __future__ import absolute_import

from ..version_info import PY3

if PY3:
    from dbm.ndbm import *
else:
    from dbm import *
