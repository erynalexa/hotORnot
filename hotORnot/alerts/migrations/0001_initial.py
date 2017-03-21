# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeatExhaustion',
            fields=[
                ('date', models.DateTimeField(primary_key=True, serialize=False)),
                ('indicator', models.IntegerField()),
            ],
            options={
                'db_table': 'heat_exhaustion',
                'managed': False,
            },
        ),
    ]
