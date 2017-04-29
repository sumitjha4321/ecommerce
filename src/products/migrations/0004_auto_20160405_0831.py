# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_opinionpoll_response'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.RemoveField(
            model_name='response',
            name='poll',
        ),
        migrations.DeleteModel(
            name='OpinionPoll',
        ),
        migrations.DeleteModel(
            name='Response',
        ),
    ]
