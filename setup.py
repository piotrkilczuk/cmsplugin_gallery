#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='cmsplugin_gallery',
    version='1.1.8',
    author='Piotr Kilczuk',
    author_email='piotr@tymaszweb.pl',
    url='http://github.com/centralniak',
    description = 'DjangoCMS image gallery plugin with drag&drop '
                  'reordering in admin, support for thumbnails and '
                  'jQueryTOOLS overlay.',
    packages=find_packages(),
    provides=['cmsplugin_gallery', ],
    include_package_data=True,
    install_requires = ['django-cms>=3.9.0', 'django-inline-ordering==1.0.2',
        'easy-thumbnails', 'django-filer',],
    test_suite='tests.settings.run',
)
