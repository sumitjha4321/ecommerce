# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField()),
                ('headline', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
                ('reporter', models.CharField(max_length=200)),
            ],
        ),
    ]
