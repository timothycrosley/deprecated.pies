#!/usr/bin/env python

from distutils.core import setup
import sys

install_requires = []
if sys.version < '3':
    install_requires += ['pies2overrides']

setup(name='pies',
      version='1.0.3',
      description='The simplest way to write one program that runs on both Python 2 and Python 3.',
      author='Timothy Crosley',
      author_email='timothy.crosley@gmail.com',
      url='https://github.com/timothycrosley/pies',
      download_url='https://github.com/timothycrosley/pies/blob/master/dist/pies-1.0.2.tar.gz?raw=true',
      license="GNU GPLv2",
      install_requires=install_requires,
      requires=install_requires,
      py_modules=['pies'])
