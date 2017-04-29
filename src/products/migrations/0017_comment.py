# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_productfeatured_make_background_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20, null=True, blank=True)),
                ('rating', models.DecimalField(null=True, max_digits=3, decimal_places=1, blank=True)),
                ('subject', models.CharField(default=b'Subject', max_length=120, null=True, blank=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('product', models.ForeignKey(blank=True, to='products.Product', null=True)),
            ],
        ),
    ]
