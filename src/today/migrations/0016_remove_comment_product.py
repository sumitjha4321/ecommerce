# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0015_auto_20160419_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='product',
        ),
    ]
