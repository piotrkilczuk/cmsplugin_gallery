# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='crop',
            field=models.CharField(default=b'0%', max_length=10, choices=[(b'0%', b'0%'), (b'25%', b'25%'), (b'50%', b'50%'), (b'75%', b'75%'), (b'100%', b'100%')]),
        ),
        migrations.AlterField(
            model_name='galleryplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='cmsplugin_gallery_galleryplugin', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
