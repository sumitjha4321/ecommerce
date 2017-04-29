# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20160405_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.FileField(upload_to=products.models.product_image_upload),
        ),
    ]
