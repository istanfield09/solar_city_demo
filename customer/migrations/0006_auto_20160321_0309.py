# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 03:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20160320_2010'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customer',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='birthdate',
        ),
    ]