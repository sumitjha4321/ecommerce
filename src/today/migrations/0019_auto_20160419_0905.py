# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0018_auto_20160419_0905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='products',
            new_name='product2',
        ),
    ]
