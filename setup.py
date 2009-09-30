#!/usr/bin/env python

from distutils.core import setup

from spamish import __version__ as version

setup(
    name = 'spamish',
    version = version,
    description = 'Spam filtering library for Akismet and TypePad services',
    author = 'Lefora',
    author_email = 'samuel@lefora.com',
    url = 'http://github.com/samuel/python-spamish',
    packages = ['spamish'],
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
