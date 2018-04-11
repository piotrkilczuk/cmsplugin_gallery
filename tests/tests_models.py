
# -*- coding: utf-8 -*-
from django.test import TestCase
from cmsplugin_gallery.models import GalleryPlugin, Image as GalleryImage
from django.core.files import File
import filer.fields.image

class GalleryTestCase(TestCase):

    def setUp(self):
        from filer.models import Image
        self.gallery = GalleryPlugin.objects.create(
            template='cmsplugin_gallery/gallery.html')
        img_file = File(open(u'tests/logo.png', 'rb'))
        image_instance = Image.objects.get_or_create(
                            file=img_file,
                            defaults={
                                'name': img_file.name
                            }
                        )[0]
        self.image = GalleryImage.objects.create(image_src=image_instance, gallery=self.gallery)

    def test_gallery_instance(self):
        image_instance = GalleryImage.objects.get(id=self.image.id)
        self.assertEqual(image_instance.gallery.id, self.gallery.id)
