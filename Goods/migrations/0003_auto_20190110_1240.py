# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-01-10 12:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0002_auto_20190110_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]