#!/usr/bin/env python

from __future__ import absolute_import

import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
   import pypandoc
   readme = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError, OSError, RuntimeError):
   readme = ''

setup(name='pies',
      version='2.6.7',
      description='The simplest way to write one program that runs on both Python 2 and Python 3.',
      long_description=readme,
      author='Timothy Crosley',
      author_email='timothy.crosley@gmail.com',
      url='https://github.com/timothycrosley/pies',
      download_url='https://github.com/timothycrosley/pies/blob/master/dist/pies-2.6.7.tar.gz?raw=true',
      license="MIT",
      extras_require={':python_version=="2.6" or python_version=="2.7"': ['pies2overrides', 'enum34'],
                      ':python_version=="3.0" or python_version=="3.1" or '
                      'python_version=="3.2" or python_version=="3.3"': ['enum34'],
                      ':python_version=="3.0" or python_version=="3.1" or python_version=="3.2"':
                          ['argparse', 'configparser']},
      packages=['pies'],
      keywords='Python, Python2, Python3, six, future, refactoring, single-code-base',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.0',
                   'Programming Language :: Python :: 3.1',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Utilities'])
