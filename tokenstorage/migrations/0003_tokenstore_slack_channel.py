# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokenstorage', '0002_auto_20170308_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokenstore',
            name='slack_channel',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
