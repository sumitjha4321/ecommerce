# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0011_comment_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='product',
        ),
    ]
