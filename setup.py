#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='cmsplugin_gallery',
    version='0.6.5',
    author='Piotr Kilczuk',
    author_email='piotr@tymaszweb.pl',
    url='http://github.com/centralniak',
    description = 'DjangoCMS image gallery plugin with drag&drop '
                  'reordering in admin, support for thumbnails and '
                  'jQueryTOOLS overlay.',
    packages=find_packages(),
    provides=['cmsplugin_gallery', ],
    include_package_data=True,
    install_requires = ['django-inline-ordering>=0.1.1', 'easy-thumbnails',]
)
