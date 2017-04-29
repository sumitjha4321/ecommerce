# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20160418_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='items',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
