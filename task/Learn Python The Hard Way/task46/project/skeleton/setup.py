#! /usr/bin/env python
# -*- coding:utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'My Project',
    'author' : 'xtom',
    'url' : 'xtom1024.com',
    'download_url' : 'Where to download it.',
    'author_email' : 'xtom0369@gmail.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'package' : ['NAME'],
    'script' : [],
    'name' : 'projectname'
}

setup(**config)
