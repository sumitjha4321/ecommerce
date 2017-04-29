# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20160407_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='inventory',
            field=models.IntegerField(default=-1),
        ),
    ]
