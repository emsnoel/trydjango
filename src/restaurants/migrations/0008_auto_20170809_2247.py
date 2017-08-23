# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-09 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_restaurantlocation_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='my_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
