# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name=b'\xe6\xb8\xb8\xe6\x88\x8f\xe5\x90\x8d\xe7\xa7\xb0')),
                ('types', models.CharField(max_length=30, verbose_name=b'\xe6\xb8\xb8\xe6\x88\x8f\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('date', models.DateField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f')),
                ('company', models.CharField(max_length=50, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x85\xac\xe5\x8f\xb8')),
                ('dx', models.FloatField(verbose_name=b'\xe6\xb8\xb8\xe6\x88\x8f\xe5\xa4\xa7\xe5\xb0\x8f')),
                ('introduction', models.TextField(verbose_name=b'\xe6\xb8\xb8\xe6\x88\x8f\xe7\xae\x80\xe4\xbb\x8b')),
                ('image', models.ImageField(upload_to=b'game/static/images', verbose_name=b'\xe6\xb8\xb8\xe6\x88\x8f\xe5\x9b\xbe\xe7\x89\x87')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
