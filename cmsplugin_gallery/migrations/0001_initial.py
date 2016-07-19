# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cmsplugin_gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default=b'cmsplugin_gallery/gallery-fancy.html', max_length=255, choices=[(b'cmsplugin_gallery/gallery-fancy.html', b'gallery-fancy.html'), (b'cmsplugin_gallery/gallery.html', b'gallery.html')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inline_ordering_position', models.IntegerField(null=True, blank=True)),
                ('src', models.ImageField(height_field=b'src_height', upload_to=cmsplugin_gallery.models.UploadPath(b'GalleryPlugin'), width_field=b'src_width', verbose_name='Image file')),
                ('src_height', models.PositiveSmallIntegerField(verbose_name='Image height', null=True, editable=False)),
                ('src_width', models.PositiveSmallIntegerField(verbose_name='Image height', null=True, editable=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title', blank=True)),
                ('alt', models.TextField(verbose_name='Alt text', blank=True)),
                ('gallery', models.ForeignKey(verbose_name='Gallery', to='cmsplugin_gallery.GalleryPlugin')),
            ],
            options={
                'ordering': ('inline_ordering_position',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
