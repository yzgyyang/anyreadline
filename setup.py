##############################################################################
#
# Written by Philippe Ombredanne for nexB Inc.
# Based on an idea of Marius Gedminas
# This software is placed in the Public Domain
#
##############################################################################
name = "anyreadline"
version = "0.1.1"

import os
import sys
from setuptools import setup
from distutils import sysconfig

long_description = """anyreadline tries to do the right thing and installs either 
pyreadline for Windows or gnureadline for other platforms if the stdlib version
wasn't built in."""

sysplat = str(sys.platform).lower()
have_libreadline = sysconfig.get_config_var('HAVE_LIBREADLINE')

if not have_libreadline:
    install_requires = ['setuptools'] 
    if 'win32' in sysplat:
        install_requires += ['pyreadline'] 
    else:
        install_requires += ['gnureadline']

setup(
    name = name,
    version = version,
    author = "Philippe Ombredanne for nexB Inc.",
    author_email = "pom@nexb.com",
    description = "readline on most OS",
    long_description = long_description,
    license = "Public Domain",
    keywords = "readline pyreadline",
    url='https://github.com/pombredanne/anyreadline',
    
    data_files = [('.', ['README.md'])],
    install_requires = install_requires,
    include_package_data = True,
    zip_safe=False,
    classifiers = [
       'Environment :: Console',
       'License :: Public Domain',
       'Programming Language :: Python',
       'Programming Language :: Python :: 2',
       ],
    )

