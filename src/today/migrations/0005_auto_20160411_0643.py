# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0004_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.IntegerField(),
        ),
    ]
