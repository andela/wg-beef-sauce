# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-08 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20180808_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='reg_flag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authtoken.Token'),
        ),
    ]
