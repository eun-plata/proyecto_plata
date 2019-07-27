# -*- coding: utf-8 -*-

# Este código es parte de Duplik2.
#
# (C) Copyright Eun Young Cho, 2019.

import setuptools
import inspect
import sys
import os

long_description = os.path.join(os.path.dirname(__file__), "README.rst")
with open(long_description, "r") as l_description:
    LONG_DESCRIPTION = l_description.read()

if not hasattr(setuptools, 'find_namespace_packages') or not inspect.ismethod(setuptools.find_namespace_packages):
    print("Your setuptools version:'{}' does not support PEP 420 (find_namespace_packages). "
          "Upgrade it to version >='40.1.0' and repeat install.".format(setuptools.__version__))
    sys.exit(1)

VERSION_PATH = os.path.join(os.path.dirname(__file__), "VERSION.txt")
with open(VERSION_PATH, "r") as version_file:
    VERSION = version_file.read().strip()

setuptools.setup(
    name='proyecto_plata',
    version=VERSION,
    description='Duplik2: Busca duplicados de una carpeta',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/eun-plata/proyecto_plata',
    author='Eun Young Cho',
    author_email='eyoung.cho@gmail.com',
    license='The Unlicense',
    classifiers=(
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utils"
    ),
    keywords='proyecto_plata archivo file repetidos carpeta',
    packages=setuptools.find_packages(exclude=['test*']),
    include_package_data=True,
    python_requires=">=3.7",
    extras_require={
        'torch': ["torch; sys_platform != 'win32'"],
    }
)