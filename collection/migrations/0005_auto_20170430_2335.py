# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 23:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_city_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'States'},
        ),
        migrations.RemoveField(
            model_name='city',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='city',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='city',
            name='user',
        ),
        migrations.AlterField(
            model_name='city',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Profile'),
        ),
    ]
