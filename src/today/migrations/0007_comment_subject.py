# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.CharField(default=b'Subject', max_length=120),
        ),
    ]
