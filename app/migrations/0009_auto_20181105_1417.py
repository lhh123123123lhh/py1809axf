# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-05 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.CharField(default=1, max_length=10),
        ),
        migrations.AlterModelTable(
            name='user',
            table='axf_user',
        ),
    ]