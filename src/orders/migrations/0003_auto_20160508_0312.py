# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20160508_0309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='usercheckout',
            new_name='user',
        ),
    ]
