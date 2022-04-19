# Cmsplugin Gallery

[![Run Tests](https://github.com/piotrkilczuk/cmsplugin_gallery/actions/workflows/test.yml/badge.svg)](https://github.com/piotrkilczuk/cmsplugin_gallery/actions/workflows/test.yml)

`cmsplugin_gallery` is the most versatile gallery plugin for djangoCMS. It supports
Python3.7 and above.

Features:

- Latest version of the plugin supports filer.
- Drag & Drop reordering of photos in the plugin admin
- Unlimited, auto-discovered custom templates - you can change template
  of given gallery at anytime, use javascript galleries etc.


## Requirements

Supports Django version 3.2+ and latest Django CMS version.
Follow individual installation instructions before installing **cmsplugin_gallery**.
Please note that cmsplugin_gallery requires:

- django-inline-ordering http://pypi.python.org/pypi/django-inline-ordering/
- easy-thumbnails http://pypi.python.org/pypi/easy-thumbnails/
- django-filer https://pypi.python.org/pypi/django-filer

**IMPORTANT**

If you are using version later than 1.1.4, Please update all your templates to use
`image_src` instead of `src`. `image_src` is the new FilerImageField instead of the old
`src` which was the ImageField. Check this [diff](https://github.com/centralniak/cmsplugin_gallery/commit/364378842885ba2e2e0f2730076658b3c039534c) for the change in sample template.

## Installation

- `pip install cmsplugin_gallery`
- Add `'cmsplugin_gallery'` to `INSTALLED_APPS` (if necessary)
- Run Migrations

## Usage

The easiest approach is to use a nice feature of cmsplugin_gallery -
the template autodiscovery. In order to take advantage of it, add your custom
templates in the cmsplugin_gallery subdirectory of any of template dirs scanned
by Django.

If you don't want to use the autodiscovery, you can hardcode available templates
in settings.py using following setting:

```python
CMSPLUGIN_GALLERY_TEMPLATES = (
    ('app/template.html', 'Template #1', ),
    ('app/other_template.html', 'Template #2', ),
)
```
Embed as a typical plugin.

## Bugs & Contribution

Please use GitHub to report bugs, feature requests and submit your code.

[Report New Issue](https://github.com/piotrkilczuk/cmsplugin_gallery/issues/new/choose)


## Contributors

[Contributors](https://github.com/piotrkilczuk/cmsplugin_gallery/graphs/contributors)
