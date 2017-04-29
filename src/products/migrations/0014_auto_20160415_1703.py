# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20160415_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
