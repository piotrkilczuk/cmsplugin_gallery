# encoding: utf-8
#import datetime

import os

from south.db import db
from south.v2 import DataMigration
from django.conf import settings
from django.core.files import File
from django.db import models

from cmsplugin_gallery.models import Image

class Migration(DataMigration):

    classes = (models.ImageField, models.FileField, )
    fields = ('src', )

    def resave_files(self, object):
        for field in self.fields:
            field_callable = getattr(object, field)
            absfilepath = os.path.join(settings.MEDIA_ROOT, field_callable.name)
            filename = os.path.basename(absfilepath)
            f = File(open(absfilepath, 'r'))
            field_callable.save(filename, f)
            f.close()

    def forwards(self, orm):
        objects = orm['cmsplugin_gallery.Image'].objects.all()
        for object in objects:
            self.resave_files(object)

    backwards = forwards

    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_gallery.galleryplugin': {
            'Meta': {'object_name': 'GalleryPlugin', 'db_table': "'cmsplugin_galleryplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'cmsplugin_gallery/gallery.html'", 'max_length': '255'})
        },
        'cmsplugin_gallery.image': {
            'Meta': {'ordering': "('inline_ordering_position',)", 'object_name': 'Image'},
            'alt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_gallery.GalleryPlugin']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inline_ordering_position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'src': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'src_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'src_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_gallery']
