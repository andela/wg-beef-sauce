# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-17 08:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_auto_20180817_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutlog',
            name='session',
        ),
        migrations.AddField(
            model_name='workoutsession',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.WorkoutLog', verbose_name='WorkoutLog'),
        ),
    ]
