# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_productfeatured_make_background_image'),
        ('today', '0008_auto_20160419_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(default='iPhone', to='products.Product'),
            preserve_default=False,
        ),
    ]
