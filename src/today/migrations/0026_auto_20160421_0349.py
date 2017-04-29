# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0025_auto_20160419_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_joined', models.DateField()),
                ('invite_reason', models.CharField(max_length=64)),
                ('group', models.ForeignKey(to='today.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(to='today.Person'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(to='today.Person', through='today.Membership'),
        ),
    ]
