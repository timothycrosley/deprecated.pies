#!/usr/bin/env python

from distutils.core import setup

setup(name='pies',
      version='1.0.0',
      description='The simplest way to write one program that runs on both Python 2 and Python 3.',
      author='Timothy Crosley',
      author_email='timothy.crosley@gmail.com',
      url='http://www.simpleinnovation.org/',
      download_url='https://github.com/timothycrosley/SortImports/blob/master'
                   '/dist/SortImports-0.1.tar.gz?raw=true',
      license="GNU GPLv2",
      install_requires=['ordereddict'],
      requires=['ordereddict'],
      py_modules=['pies'])
