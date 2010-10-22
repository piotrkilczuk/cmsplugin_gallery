import admin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
import models 


class CMSGalleryPlugin(CMSPluginBase):
    
    model = models.GalleryPlugin
    inlines = [admin.ImageInline,]
    name = _('Image gallery')
    render_template = 'cmsplugin_gallery/gallery.html'
    
    def render(self, context, instance, placeholder):
        context.update({'images': instance.image_set.all(), 'gallery': instance})
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(CMSGalleryPlugin)