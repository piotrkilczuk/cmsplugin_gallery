from __future__ import absolute_import
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from . import admin
from . import models


class CMSGalleryPlugin(CMSPluginBase):

    model = models.GalleryPlugin
    inlines = [admin.ImageInline, ]
    name = _('Image gallery Plugin')
    module = 'Generiek'
    render_template = 'cmsplugin_gallery/gallery.html'

    def render(self, context, instance, placeholder):
        images = instance.image_set.all()
        grouped_images = [images[i:i + 4] for i in xrange(0, len(images.values_list('src')), 4)]
        context.update({
                        'images': instance.image_set.all(),
                        'grouped_images': grouped_images,
                        'gallery': instance,
                       })
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(CMSGalleryPlugin)
