# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-08 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restrict',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='restrict',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
