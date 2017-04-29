# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20160511_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(related_name='billing_address', to='orders.UserAddress', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(related_name='shipping_address', to='orders.UserAddress', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to='orders.UserCheckOut', null=True),
        ),
    ]
