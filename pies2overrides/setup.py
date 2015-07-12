#!/usr/bin/env python

from __future__ import absolute_import

import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='pies2overrides',
      version='2.6.7',
      description='Defines override classes that should be included with pies only if running on Python2.',
      author='Timothy Crosley',
      author_email='timothy.crosley@gmail.com',
      url='https://github.com/timothycrosley/pies',
      download_url='https://github.com/timothycrosley/pies/blob/master/pies2overrides/dist/pies2overrides-2.6.7.tar.gz?raw=true',
      license="MIT",
      install_requires=['ipaddress'],
      requires=['ipaddress'],
      extras_require={':python_version=="2.6"': ['ordereddict', 'argparse']},
      py_modules=['configparser', 'builtins', 'copyreg', 'queue', 'reprlib', 'socketserver'],
      packages=['html', 'http', 'xmlrpc'])
