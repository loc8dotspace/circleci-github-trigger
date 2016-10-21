# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triggers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='triggerevent',
            name='branch',
            field=models.CharField(default='master', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triggerevent',
            name='build_url',
            field=models.URLField(null=True),
        ),
    ]
