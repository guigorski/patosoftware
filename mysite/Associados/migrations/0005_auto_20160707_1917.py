# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Associados', '0004_auto_20160707_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associados',
            name='CPF',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='associados',
            name='RA',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='associados',
            name='RG',
            field=models.CharField(max_length=12),
        ),
    ]
