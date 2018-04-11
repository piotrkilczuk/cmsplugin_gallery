# -*- coding: utf-8 -*-
from django.test import TestCase
from cmsplugin_gallery.models import GalleryPlugin, Image
from django.core.files import File

class GalleryTestCase(TestCase):

    def setUp(self):
        self.gallery = GalleryPlugin.objects.create(
            template='cmsplugin_gallery/gallery.html')
        self.image = Image.objects.create(src=File(open('tests/logo.png')), gallery=self.gallery)

    def test_gallery_instance(self):
        image_instance = Image.objects.get(id=self.image.id)
        self.assertEqual(image_instance.gallery.id, self.gallery.id)
