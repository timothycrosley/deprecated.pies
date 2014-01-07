from __future__ import absolute_import

from ast import *

from .version_info import PY2

if PY2:
    Try = TryExcept

    def argument_names(node):
        return [isinstance(arg, Name) and arg.id or None for arg in node.args.args]

    def kw_only_argument_names(node):
        return []

    def kw_only_default_count(node):
        return 0
else:
    TryFinally = ()

    def argument_names(node):
        return [arg.arg for arg in node.args.args]

    def kw_only_argument_names(node):
        return [arg.arg for arg in node.args.kwonlyargs]

    def kw_only_default_count(node):
        return sum(1 for n in node.args.kw_defaults if n is not None)
