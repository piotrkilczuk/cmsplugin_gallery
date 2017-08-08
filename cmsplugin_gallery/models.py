from datetime import date
import os
import threading

from cms.models import CMSPlugin
from cms.utils import get_cms_setting
from django.db import models
from django.utils.translation import ugettext_lazy as _
from inline_ordering.models import Orderable
from django.utils.deconstruct import deconstructible
from django.db import connection

import utils

localdata = threading.local()
localdata.TEMPLATE_CHOICES = utils.autodiscover_templates()
TEMPLATE_CHOICES = localdata.TEMPLATE_CHOICES


@deconstructible
class UploadPath(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        return "gallery/%s/%s" % (instance.title, filename)

get_upload_path = UploadPath('GalleryPlugin')

class GalleryPlugin(CMSPlugin):

    def copy_relations(self, oldinstance):
        for img in oldinstance.image_set.all():
            new_img = Image()
            new_img.gallery=self
            new_img.src = img.src
            new_img.src_height = img.src_height
            new_img.src_width = img.src_width
            new_img.title = img.title
            new_img.alt = img.alt
            new_img.save()

    template = models.CharField(max_length=255,
                                choices=TEMPLATE_CHOICES,
                                default=TEMPLATE_CHOICES[0][0],
                                editable=len(TEMPLATE_CHOICES) > 1)

    def __unicode__(self):
        return _(u'%(count)d image(s) in gallery') % {'count': self.image_set.count()}


class Image(Orderable):

    def get_media_path(self, filename):
        pages = self.gallery.placeholder.page_set.all()
        if pages.count():
            return pages[0].get_media_path(filename)
        else:
            today = date.today()
            return os.path.join(get_cms_setting('PAGE_MEDIA_PATH'),
                str(today.year), str(today.month), str(today.day), filename)

    gallery = models.ForeignKey(GalleryPlugin, verbose_name=_("Gallery"))
    src = models.ImageField(_("Image file"), upload_to=get_upload_path,
                            height_field='src_height',
                            width_field='src_width')
    src_height = models.PositiveSmallIntegerField(_("Image height"), editable=False, null=True)
    src_width = models.PositiveSmallIntegerField(_("Image height"), editable=False, null=True)
    title = models.CharField(_("Title"), max_length=255, blank=True)
    alt = models.TextField(_("Alt text"), blank=True)

    def __unicode__(self):
        return self.title or self.alt or str(self.pk)
