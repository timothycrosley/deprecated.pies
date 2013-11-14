#!/usr/bin/env python

from __future__ import absolute_import

import sys
from distutils.core import setup

install_requires = []
if sys.version < '3':
    install_requires += ['pies2overrides==2.0.0']
elif sys.version < '3.2':
    install_requires += ['argparse']

if sys.version < '3.4':
    install_requires += ['enum34']

setup(name='pies',
      version='2.0.0',
      description='The simplest way to write one program that runs on both Python 2 and Python 3.',
      author='Timothy Crosley',
      author_email='timothy.crosley@gmail.com',
      url='https://github.com/timothycrosley/pies',
      download_url='https://github.com/timothycrosley/pies/blob/master/dist/pies-1.0.2.tar.gz?raw=true',
      license="MIT",
      install_requires=install_requires,
      requires=install_requires,
      py_modules=['pies'])
