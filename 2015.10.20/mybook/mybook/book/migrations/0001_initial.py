# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=50)),
                ('passwd', models.TextField(max_length=18)),
                ('degree', models.NullBooleanField()),
                ('age', models.NullBooleanField()),
                ('gender', models.CharField(max_length=20)),
                ('comment', models.TextField()),
                ('hobby', models.TextField()),
                ('major', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
