from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from inline_ordering.models import Orderable


class GalleryPlugin(CMSPlugin):
    
    def __unicode__(self):
        return _(u'%(count)d image(s) in gallery') % {'count': self.image_set.count()}


class Image(Orderable):
    
    gallery = models.ForeignKey(GalleryPlugin)
    src = models.ImageField(upload_to='cmsplugin_gallery/images', 
                            height_field='src_height', 
                            width_field='src_width')
    src_height = models.PositiveSmallIntegerField(editable=False, null=True)
    src_width = models.PositiveSmallIntegerField(editable=False, null=True)
    title = models.CharField(max_length=255, blank=True)
    alt = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.title or self.alt or str(self.pk)