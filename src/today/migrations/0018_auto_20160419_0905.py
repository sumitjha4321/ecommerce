# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0017_comment_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='product',
            new_name='products',
        ),
    ]
