# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 01:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 4, 20, 56, 19, 457000)),
        ),
    ]