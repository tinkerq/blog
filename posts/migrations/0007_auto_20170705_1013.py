# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-05 10:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 7, 5, 10, 13, 24, 156182, tzinfo=utc)),
            preserve_default=False,
        ),
    ]