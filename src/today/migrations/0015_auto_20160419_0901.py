# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_productfeatured_make_background_image'),
        ('today', '0014_auto_20160419_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(blank=True, to='products.Product', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.DecimalField(default=1.0, max_digits=3, decimal_places=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.CharField(default=b'Subject', max_length=120),
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default='none', max_length=20),
            preserve_default=False,
        ),
    ]
