# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-20 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20160221_0311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerId', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=64)),
                ('lastName', models.CharField(max_length=64)),
                ('birthdate', models.DateField()),
                ('streetAddress', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=18)),
                ('zipcode', models.PositiveIntegerField()),
                ('contactDate', models.DateField()),
                ('contactMessage', models.TextField()),
            ],
            managers=[
                ('customers', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='CustomerData',
        ),
    ]
