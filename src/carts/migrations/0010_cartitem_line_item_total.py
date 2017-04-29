# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_auto_20160418_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='line_item_total',
            field=models.DecimalField(default=19.99, max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
    ]
