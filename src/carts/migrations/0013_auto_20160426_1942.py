# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0012_auto_20160426_0424'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax_total',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
