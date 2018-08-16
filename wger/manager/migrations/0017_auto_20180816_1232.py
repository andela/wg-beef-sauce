# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-16 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0016_auto_20180816_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='period',
            field=models.CharField(choices=[('null', 'No period'), ('Microcycle', 'Microcycle(1 week)'), ('Mesocycle', 'Mesocycle(2-6 weeks)'), ('Macrocycle', 'Macrocycle(1 year)')], max_length=50, null=True, verbose_name='Period'),
        ),
    ]
