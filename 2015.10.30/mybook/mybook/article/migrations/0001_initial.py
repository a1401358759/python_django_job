# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98')),
                ('author', models.CharField(max_length=30, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe4\xbd\x9c\xe8\x80\x85')),
                ('content', models.TextField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9')),
                ('date', models.DateField(verbose_name=b'\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xa5\xe6\x9c\x9f')),
                ('img', models.ImageField(upload_to=b'article/static/images', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\x8f\x92\xe5\x9b\xbe')),
                ('hot', models.IntegerField(verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe7\x8e\x87')),
                ('src', models.CharField(max_length=70, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe9\x93\xbe\xe6\x8e\xa5')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
