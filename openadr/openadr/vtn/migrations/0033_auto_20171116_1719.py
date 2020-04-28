# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-16 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtn', '0032_auto_20171115_2149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drevent',
            options={'verbose_name': 'DR event', 'verbose_name_plural': 'DR Events'},
        ),
        migrations.AlterModelOptions(
            name='drprogram',
            options={'verbose_name': 'DR program', 'verbose_name_plural': 'DR Programs'},
        ),
        migrations.AlterField(
            model_name='site',
            name='phone_number',
            field=models.CharField(max_length=13, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='siteevent',
            name='notification_sent_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Notification Sent Time'),
        ),
    ]
