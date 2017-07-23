#! /usr/bin/env python
# -*- coding:utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'ex17',
    'author' : 'xtom',
    'url' : 'xtom1024.com',
    'download_url' : 'Where to download it.',
    'author_email' : 'xtom0369@gmail.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'package' : ['ex17'],
    'script' : [],
    'name' : 'ex17'
}

setup(**config)
