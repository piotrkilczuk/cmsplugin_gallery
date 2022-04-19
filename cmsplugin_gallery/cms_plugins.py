from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from . import admin
from . import models

if hasattr(settings, 'GALLERY_PLUGIN_MODULE_NAME'):
    MODULE_NAME = settings.GALLERY_PLUGIN_MODULE_NAME
else:
    MODULE_NAME = 'UI'

class CMSGalleryPlugin(CMSPluginBase):

    model = models.GalleryPlugin
    inlines = [admin.ImageInline, ]
    name = _('Image gallery Plugin')
    module = MODULE_NAME
    render_template = 'cmsplugin_gallery/gallery.html'

    def render(self, context, instance, placeholder):
        images = instance.image_set.all()
        grouped_images = [images[i:i + 4] for i in range(0, len(images.values_list('image_src')), 4)]
        context.update({
                        'images': instance.image_set.all(),
                        'grouped_images': grouped_images,
                        'gallery': instance,
                       })
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(CMSGalleryPlugin)
