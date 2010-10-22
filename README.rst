======================================
DjangoCMS Gallery plugin (yet another)
======================================

Features
--------

1. Drag&Drop reordering of photos

2. Unlimited, auto-discovered custom templates - you can change template 
   of given gallery at anytime, use javascript galleries etc. 

Requirements
------------

- django-inline-ordering http://pypi.python.org/pypi/django-inline-ordering/
- easy-thumbnails http://pypi.python.org/pypi/easy-thumbnails/

Installation
------------

1. Install requirements and put ``cmsplugin_gallery`` on your python path (should be 
   installed automatically if you use ``easy_install`` / ``pip``).

2. Add ``cmsplugin_gallery`` to your installed apps

3. Run ``syncdb`` or ``migrate cmsplugin_gallery`` (if you use South). 

4. Create directory for storing media files - files will be uploaded to MEDIA_ROOT + 'cmsplugin_gallery/images'.
   Make sure it is writable especially when running in embedded mode on production server. 

5. Very simple template is included with the project. To make it work 100%, install jQueryTOOLS 
   for overlay support using your favorite method
   http://flowplayer.org/tools/download/index.html

Usage
-----

In order to embed your custom templates, put it under ``templates/cmsplugin_gallery/YOURTEMPLATE.html``
in any active application directory or directory specified in ``TEMPLATE_DIRS``. 

Embed as a typical plugin.