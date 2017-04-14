#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

import os
from setuptools import setup

version = '0.0'
long_description_filename = os.path.join(
    os.path.dirname(__file__), 'README.rst')
long_description = open(long_description_filename).read()

setup(
    name="miniSim",
    version=version,
    author="Julián U. da Silva Gillig",
    url="https://github.com/msabramo/miniSim",
    keywords='robotics simulation educational python',
    description="Robot simulation forked from miniBloq at https://github.com/miniBloq/v0.83",
    long_description=long_description,
    license='RobotGroup – Multiplo Pacifist License (RMPL) 1.0',
    install_requires=['pygame'],
    py_modules=['miniSim'],
    zip_safe=False,
)
