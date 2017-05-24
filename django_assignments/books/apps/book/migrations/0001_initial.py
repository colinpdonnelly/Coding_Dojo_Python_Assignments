# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
