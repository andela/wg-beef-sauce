# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-08 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20180808_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='create_use_rest_api',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
