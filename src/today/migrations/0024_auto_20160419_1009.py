# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0023_auto_20160419_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='product',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
