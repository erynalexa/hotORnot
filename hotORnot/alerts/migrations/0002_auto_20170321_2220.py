# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 02:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='heatexhaustion',
            table='heat_exhaustion',
        ),
    ]
