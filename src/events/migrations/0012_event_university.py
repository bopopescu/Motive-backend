# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 09:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='university',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='events.University'),
        ),
    ]
