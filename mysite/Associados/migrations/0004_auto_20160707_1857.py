# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 21:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Associados', '0003_auto_20160707_1855'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Associados',
        ),
    ]