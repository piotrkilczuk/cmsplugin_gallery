#!/usr/bin/env python

from setuptools import find_packages, setup


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Framework :: Django',
    'Framework :: Django :: 2.2',
    'Framework :: Django :: 3.1',
    'Framework :: Django :: 3.2',
    'Framework :: Django CMS',
    'Framework :: Django CMS :: 3.9',
    'Framework :: Django CMS :: 3.10',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("History.md") as history_file:
    history = history_file.read()

from cmsplugin_gallery import __version__

setup(
    name='cmsplugin_gallery',
    version=__version__,
    author='Piotr Kilczuk',
    author_email='piotr@tymaszweb.pl',
    url='https://github.com/piotrkilczuk/cmsplugin_gallery',
    description = 'DjangoCMS image gallery plugin with drag&drop '
                  'reordering in admin, support for thumbnails and '
                  'jQueryTOOLS overlay.',
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    provides=['cmsplugin_gallery', ],
    include_package_data=True,
    install_requires = ['django-cms>=3.9.0', 'django-inline-ordering==1.0.2',
        'easy-thumbnails', 'django-filer',],
    test_suite='tests.settings.run',
)
