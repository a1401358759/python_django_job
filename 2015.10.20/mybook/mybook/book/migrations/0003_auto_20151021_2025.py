# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20151021_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe4\xb9\xa6\xe5\x90\x8d')),
                ('author', models.CharField(max_length=30, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('date', models.DateField(verbose_name=b'\xe5\x87\xba\xe7\x89\x88\xe6\x97\xa5\xe6\x9c\x9f')),
                ('price', models.FloatField(verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('publisher', models.CharField(max_length=50, verbose_name=b'\xe5\x87\xba\xe7\x89\x88\xe7\xa4\xbe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
