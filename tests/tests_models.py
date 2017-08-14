# -*- coding: utf-8 -*-
from django.test import TestCase
from cmsplugin_gallery.models import GalleryPlugin, Image


class GalleryTestCase(TestCase):

    def setUp(self):
        self.gallery = GalleryPlugin.objects.create(
            template='cmsplugin_gallery/gallery.html')
        self.image = Image.objects.create(src='cms_page_media/110/123.jpg', gallery=self.gallery)

    def test_gallery_instance(self):
        image_instance = Image.objects.get(src='cms_page_media/110/123.jpg')
        self.assertEqual(image_instance.gallery.id, self.gallery.id)
