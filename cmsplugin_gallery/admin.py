from inline_ordering.admin import OrderableStackedInline
from . import forms
from . import models


class ImageInline(OrderableStackedInline):

    model = models.Image

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image_src':
            kwargs.pop('request', None)
            kwargs['widget'] = forms.AdminImageWidget
            return db_field.formfield(**kwargs)
        return super().\
            formfield_for_dbfield(db_field, **kwargs)
