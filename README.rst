======================================
DjangoCMS Gallery plugin (yet another)
======================================

Requirements
------------

- django-inline-ordering http://pypi.python.org/pypi/django-inline-ordering/
- easy-thumbnails http://pypi.python.org/pypi/easy-thumbnails/

Installation
------------

1. Install requirements and put cmsplugin_gallery on your python path

2. Add ``cmsplugin_gallery`` to your installed apps

2. Run syncdb 

3. Create directory for storing media files - files will be uploaded to MEDIA_ROOT + 'cmsplugin_gallery/images'.
   Make sure it is writable especially when running in embedded mode on production server. 

4. Install jQueryTOOLS for overlay support using your favorite method
   http://flowplayer.org/tools/download/index.html

Usage
-----

Embed as a typical plugin.

Known issues
------------

- The template, at this point, is site-wide. Autodiscovery of templates could make sense. 