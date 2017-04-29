# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0007_comment_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.DecimalField(default=1, max_digits=3, decimal_places=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default='none', max_length=20),
            preserve_default=False,
        ),
    ]
