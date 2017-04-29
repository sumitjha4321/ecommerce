# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0011_cart_subtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
