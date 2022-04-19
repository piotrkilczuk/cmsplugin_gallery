#!/usr/bin/env python
# -*- coding: utf-8 -*-

HELPER_SETTINGS = {
    'INSTALLED_APPS': [
        'easy_thumbnails',
        'filer',
        'mptt',
    ],
    'ALLOWED_HOSTS': ['localhost'],
    'CMS_LANGUAGES': {
        1: [{
            'code': 'en',
            'name': 'English',
        }]
    },
    'LANGUAGE_CODE': 'en',
    'DEFAULT_AUTO_FIELD': 'django.db.models.AutoField',
    'SECRET_KEY': 'herozyz',
    'GALLERY_PLUGIN_MODULE_NAME': 'UI',
    'CMSPLUGIN_GALLERY_TEMPLATES': [
        ('cmsplugin_gallery/gallery.html', 'gallery.html'),
    ]
}

def run():
    from djangocms_helper import runner
    runner.cms('cmsplugin_gallery')

if __name__ == '__main__':
    run()

