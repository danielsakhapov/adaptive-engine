# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0010_auto_20161014_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='manual',
            field=models.BooleanField(default=False),
        ),
    ]
