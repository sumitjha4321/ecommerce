# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_variation_inventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('active', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='products.Category', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='default',
            field=models.ForeignKey(related_name='default_category', blank=True, to='products.Category', null=True),
        ),
    ]
