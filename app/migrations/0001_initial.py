# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-11-28 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, verbose_name='Username')),
                ('tname', models.CharField(max_length=200, verbose_name='Task Name')),
                ('des', models.CharField(max_length=200, verbose_name='Description')),
            ],
        ),
    ]