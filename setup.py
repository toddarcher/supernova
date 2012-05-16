#!/usr/bin/python
#
# Copyright 2012 Major Hayden
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='supernova',
    version='0.5.1',
    author='Major Hayden',
    author_email='major@mhtx.net',
    description="novaclient wrapper for multiple nova environments",
    packages=['supernova'],
    url='https://github.com/rackerhacker/supernova',
    include_package_data=True,
    long_description=read('README.md'),
    entry_points={
        'console_scripts': ['supernova = supernova.supernova:bin_helper']
        }
    )