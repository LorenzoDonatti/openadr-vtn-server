# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtn', '0053_auto_20171201_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=13, null=True, verbose_name='Phone Number'),
        ),
    ]
