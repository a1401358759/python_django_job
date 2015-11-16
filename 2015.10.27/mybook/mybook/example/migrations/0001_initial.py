# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('age', models.CharField(max_length=10, verbose_name=b'\xe5\xb9\xb4\xe9\xbe\x84')),
                ('grade', models.CharField(max_length=10, verbose_name=b'\xe5\xb9\xb4\xe7\xba\xa7')),
                ('address', models.CharField(max_length=30, verbose_name=b'\xe4\xbd\x8f\xe5\x9d\x80')),
                ('photo', models.ImageField(upload_to=b'images/s/photo', verbose_name=b'\xe7\x9b\xb8\xe7\x89\x87')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('age', models.CharField(max_length=10, verbose_name=b'\xe5\xb9\xb4\xe9\xbe\x84')),
                ('project', models.CharField(max_length=10, verbose_name=b'\xe7\xa7\x91\xe7\x9b\xae')),
                ('address', models.CharField(max_length=30, verbose_name=b'\xe4\xbd\x8f\xe5\x9d\x80')),
                ('photo', models.ImageField(upload_to=b'images/s/photo', verbose_name=b'\xe7\x9b\xb8\xe7\x89\x87')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
