# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe7\x8e\xa9\xe5\xae\xb6\xe5\xa7\x93\xe5\x90\x8d')),
                ('gender', models.CharField(max_length=4, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('paiming', models.CharField(max_length=10, verbose_name=b'\xe7\x8e\xa9\xe5\xae\xb6\xe7\xad\x89\xe7\xba\xa7')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
