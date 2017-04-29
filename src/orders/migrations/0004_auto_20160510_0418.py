# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0013_auto_20160426_1942'),
        ('orders', '0003_auto_20160508_0312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shipping_total_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('order_total', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='address2',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(related_name='billing_address', to='orders.UserAddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(to='carts.Cart'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(related_name='shipping_address', to='orders.UserAddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to='orders.UserCheckOut'),
        ),
    ]
