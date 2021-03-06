# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_id', models.IntegerField()),
                ('repo_url', models.URLField(max_length=255)),
                ('parallelism', models.IntegerField()),
                ('branch', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TriggerEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commit', models.CharField(max_length=64)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('trigger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='triggers.Trigger')),
            ],
        ),
    ]
