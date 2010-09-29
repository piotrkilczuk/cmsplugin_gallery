#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='cmsplugin_gallery',
    version='0.1.1',
    author='Piotr Kilczuk',
    author_email='p.kilczuk@neumea.pl',
    url='http://github.com/centralniak',
    description = 'DjangoCMS image gallery plugin with drag&drop reordering in admin,' \
                  'support for thumbnails and jQueryTOOLS overlay.',
    packages = find_packages(),
    provides = ['cmsplugin_gallery (0.1.1)',],
    include_package_data=True,
    requires = ['inline_ordering (>=0.1.1)', 'easy_thumbnails']
)