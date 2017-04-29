# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20160510_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_total_price',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
        ),
    ]
