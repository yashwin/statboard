# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170317_2041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metric',
            old_name='data',
            new_name='data_str',
        ),
        migrations.AlterField(
            model_name='metric',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
