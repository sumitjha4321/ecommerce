# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0002_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='title',
            field=models.CharField(max_length=100, choices=[(b'MR', b'Mr.'), (b'MRS', b'Mrs.'), (b'MS', b'Ms.')]),
        ),
    ]
