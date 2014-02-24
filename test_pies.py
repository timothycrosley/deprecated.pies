from __future__ import absolute_import, division, print_function, unicode_literals

from pies.overrides import *


def test_u():
    assert u('Bj\xf6rk Gu\xf0mundsd\xf3ttir') == 'Bj\xf6rk Gu\xf0mundsd\xf3ttir'
