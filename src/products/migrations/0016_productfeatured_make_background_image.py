# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_productfeatured'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfeatured',
            name='make_background_image',
            field=models.BooleanField(default=False),
        ),
    ]
