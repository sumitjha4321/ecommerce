# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0020_auto_20160419_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.DecimalField(null=True, max_digits=3, decimal_places=1, blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.CharField(default=b'Subject', max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
