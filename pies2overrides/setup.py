#!/usr/bin/env python

from __future__ import absolute_import

import sys
from distutils.core import setup

install_requires = ['ipaddress']
if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    install_requires += ['ordereddict', 'argparse']

setup(name='pies2overrides',
      version='2.0.0',
      description='Defines override classes that should be included with pies only if running on Python2.',
      author='Timothy Crosley',
      author_email='timothy.crosley@gmail.com',
      url='https://github.com/timothycrosley/pies',
      download_url='https://github.com/timothycrosley/pies/blob/master/pies2overrides/dist/pies2overrides-2.0.0.tar.gz?raw=true',
      license="MIT",
      install_requires=install_requires,
      requires=install_requires,
      py_modules=['configparser', 'builtins', '_thread', 'copyreg', 'queue', 'reprlib', 'socketserver'],
      packages=['html', 'http', 'xmlrpc'])
