# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0013_comment_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='product',
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
            name='username',
        ),
    ]
