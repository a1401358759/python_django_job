# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20151104_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='photo',
            field=models.ImageField(upload_to=b'static/img/child', verbose_name=b'\xe7\x85\xa7\xe7\x89\x87'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mother',
            name='photo',
            field=models.ImageField(upload_to=b'static/img/mother', verbose_name=b'\xe7\x85\xa7\xe7\x89\x87'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to=b'static/img/student', verbose_name=b'\xe7\x85\xa7\xe7\x89\x87'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(upload_to=b'static/img/teacher', verbose_name=b'\xe7\x85\xa7\xe7\x89\x87'),
            preserve_default=True,
        ),
    ]
