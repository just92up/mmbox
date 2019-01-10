# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-01-10 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgaddr', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('picture', models.CharField(max_length=128)),
                ('introduce', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('token', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='user',
            field=models.ManyToManyField(to='Goods.User'),
        ),
    ]
