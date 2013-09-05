#!/usr/bin/env python

from distutils.core import setup

setup(name='pies2overrides',
      version='1.0.0',
      description='Defines override classes that should be included with pies only if running on Python2.',
      author='Timothy Crosley',
      author_email='timothy.crosley@gmail.com',
      url='https://github.com/timothycrosley/pies',
      download_url='https://github.com/timothycrosley/pies/blob/master/pies2overrides/dist/pies2overrides-1.0.0.tar.gz?raw=true',
      license="GNU GPLv2",
      install_requires=['ordereddict', 'argparse'],
      requires=['ordereddict', 'argparse'],
      py_modules=['configparser'])
