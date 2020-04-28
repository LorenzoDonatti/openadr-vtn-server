# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 16:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtn', '0015_auto_20171108_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteevent',
            name='previous_version',
        ),
        migrations.AlterField(
            model_name='drevent',
            name='last_status_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 9, 16, 1, 31, 572390), null=True, verbose_name='Last Status Time'),
        ),
        migrations.AlterField(
            model_name='siteevent',
            name='last_opt_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 9, 16, 1, 31, 573665), null=True, verbose_name='Last opt-in'),
        ),
        migrations.AlterField(
            model_name='siteevent',
            name='last_status_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 9, 16, 1, 31, 573533), verbose_name='Last Status Time'),
        ),
    ]
