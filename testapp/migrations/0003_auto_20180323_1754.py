# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20180323_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='animal_type',
            field=models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat')], max_length=16),
        ),
    ]
