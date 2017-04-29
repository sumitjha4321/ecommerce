# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20160419_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
