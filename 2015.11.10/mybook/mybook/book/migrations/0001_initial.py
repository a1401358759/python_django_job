# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('gender', models.CharField(max_length=10, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('age', models.IntegerField(verbose_name=b'\xe5\xb9\xb4\xe9\xbe\x84')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=30, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d\xe5\x8f\xb7\xe7\xa0\x81')),
                ('persion', models.ForeignKey(to='book.Persion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
