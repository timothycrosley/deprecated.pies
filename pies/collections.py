from __future__ import absolute_import

from collections import *

from .version_info import PY2

if PY2:
    from UserString import *
    from UserList import *
    from ordereddict import OrderedDict
