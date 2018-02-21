# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_gallery', '0003_auto_20170104_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='alt',
            field=models.CharField(max_length=255, verbose_name='Alt text', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='crop',
            field=models.CharField(default=b'0%', max_length=10, verbose_name=b'Positionering', choices=[(b'0%', b'0%'), (b'25%', b'25%'), (b'50%', b'50%'), (b'75%', b'75%'), (b'100%', b'100%')]),
        ),
    ]
