======================================
DjangoCMS Gallery plugin (yet another)
======================================

Features
--------

1. Drag&Drop reordering of photos in the plugin admin

2. Unlimited, auto-discovered custom templates - you can change template 
   of given gallery at anytime, use javascript galleries etc. 

Requirements
------------

- django-inline-ordering http://pypi.python.org/pypi/django-inline-ordering/
- easy-thumbnails http://pypi.python.org/pypi/easy-thumbnails/

Installation
------------

1. Install requirements and put ``cmsplugin_gallery`` on your python path 
   (requirements will be installed automatically if you use ``easy_install`` or 
   ``pip``).

2. Add ``cmsplugin_gallery`` to your installed apps

3. Run ``syncdb`` or ``migrate cmsplugin_gallery`` (if you use South). 

4. Create directory for storing media files - files will be uploaded to MEDIA_ROOT + 'cmsplugin_gallery/images'.
   Make sure it is writable especially when running in embedded mode on production server. 

5. Very simple template is included with the project. To make it work 100%, install jQueryTOOLS 
   for overlay support using your favorite method
   http://flowplayer.org/tools/download/index.html

Usage
-----

The easiest approach is to use a nice feature of cmsplugin_gallery -
the template autodiscovery. In order to take advantage of it, add your custom 
templates in the cmsplugin_gallery subdirectory of any of template dirs scanned
by Django.

If you don't want to use the autodiscovery, you can hardcode available templates
in settings.py using following setting:

::

    CMSPLUGIN_GALLERY_TEMPLATES = (
        ('app/template.html', 'Template #1', ),
        ('app/other_template.html', 'Template #2', ),
    )

Embed as a typical plugin.