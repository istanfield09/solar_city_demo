# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerData',
            fields=[
                ('customerId', models.AutoField(serialize=False, primary_key=True)),
                ('firstName', models.CharField(max_length=64)),
                ('lastName', models.CharField(max_length=64)),
                ('birthdate', models.DateTimeField()),
                ('streetAddress', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=18)),
                ('zipcode', models.PositiveIntegerField()),
                ('contactDate', models.DateField()),
                ('contactMessage', models.TextField()),
                ('operatingSystem', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
