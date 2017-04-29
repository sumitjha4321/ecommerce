# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=120, choices=[(b'billing', b'Billing'), (b'shipping', b'Shipping')])),
                ('name', models.CharField(max_length=120)),
                ('mobile', models.CharField(max_length=120)),
                ('address1', models.CharField(max_length=120)),
                ('address2', models.CharField(max_length=120)),
                ('pin', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='usercheckout',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='usercheckout',
            field=models.ForeignKey(to='orders.UserCheckOut'),
        ),
    ]
