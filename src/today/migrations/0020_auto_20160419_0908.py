# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0019_auto_20160419_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='product2',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
    ]
