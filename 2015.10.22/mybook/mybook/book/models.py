#coding:utf-8
from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 30,verbose_name = '姓名')
    gender = models.CharField(max_length = 30,verbose_name = '性别')
    age = models.IntegerField(verbose_name= '年龄')

    def __unicode__(self):
        return self.name

# Create your models here.
