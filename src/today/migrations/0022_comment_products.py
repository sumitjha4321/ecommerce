# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_productfeatured_make_background_image'),
        ('today', '0021_auto_20160419_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='products',
            field=models.ForeignKey(blank=True, to='products.Product', null=True),
        ),
    ]
