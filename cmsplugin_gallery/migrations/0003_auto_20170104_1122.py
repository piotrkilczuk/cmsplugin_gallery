# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cmsplugin_gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_gallery', '0002_auto_20161223_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryplugin',
            name='overlay_image',
            field=models.ImageField(upload_to=cmsplugin_gallery.models.UploadPath(b'GalleryPlugin'), null=True, verbose_name='Overlay Image', blank=True),
        ),
        migrations.AddField(
            model_name='galleryplugin',
            name='overlay_position',
            field=models.IntegerField(default=3, choices=[(1, b'Top Left'), (2, b'Top right'), (3, b'Bottom Left'), (4, b'Bottom Right')]),
        ),
    ]
