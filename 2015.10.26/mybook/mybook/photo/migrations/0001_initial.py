# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'images', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe8\xb7\xaf\xe5\xbe\x84')),
                ('date', models.DateField(verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4')),
                ('p_class', models.CharField(max_length=30, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe5\x88\x86\xe7\xb1\xbb')),
                ('introduce', models.TextField(verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe4\xbb\x8b\xe7\xbb\x8d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
