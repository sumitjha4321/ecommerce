# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0010_cartitem_line_item_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
    ]
