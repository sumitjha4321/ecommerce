# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0022_comment_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='products',
            new_name='product',
        ),
    ]
