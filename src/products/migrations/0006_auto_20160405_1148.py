# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='sale_price',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
        ),
    ]
