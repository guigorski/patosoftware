# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 22:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=200)),
                ('RG', models.CharField(max_length=200)),
                ('CPF', models.CharField(max_length=200)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
