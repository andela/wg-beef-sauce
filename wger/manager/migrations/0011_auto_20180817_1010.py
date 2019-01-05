# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-17 07:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_workoutsession_workout_session_logs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutsession',
            name='workout_session_logs',
        ),
        migrations.AddField(
            model_name='workoutsession',
            name='session_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.WorkoutLog', verbose_name='WorkoutLog'),
        ),
    ]
