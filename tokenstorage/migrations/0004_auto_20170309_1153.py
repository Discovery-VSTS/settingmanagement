# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokenstorage', '0003_tokenstore_slack_channel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tokenstore',
            options={'ordering': ('instance_id', 'user_email')},
        ),
        migrations.AddField(
            model_name='tokenstore',
            name='user_email',
            field=models.EmailField(default='invalid@email.com', max_length=254, unique=True),
        ),
    ]
