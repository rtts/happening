# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-22 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0002_auto_20161213_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
