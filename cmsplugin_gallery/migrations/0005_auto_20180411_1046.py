# Generated by Django 1.11.12 on 2018-04-11 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cmsplugin_gallery', '0004_auto_20170118_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_src',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.FILER_IMAGE_MODEL, verbose_name='Image File'),
        ),
        migrations.AlterField(
            model_name='galleryplugin',
            name='template',
            field=models.CharField(choices=[(b'cmsplugin_gallery/gallery-fancy.html', b'gallery-fancy.html'), (b'cmsplugin_gallery/gallery-slider.html', b'gallery-slider.html'), (b'cmsplugin_gallery/gallery.html', b'gallery.html')], default=b'cmsplugin_gallery/gallery-fancy.html', max_length=255),
        ),
    ]
