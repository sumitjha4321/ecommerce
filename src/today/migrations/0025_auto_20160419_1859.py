# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0024_auto_20160419_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='article2',
            name='publications',
            field=models.ManyToManyField(to='today.Publication'),
        ),
    ]
