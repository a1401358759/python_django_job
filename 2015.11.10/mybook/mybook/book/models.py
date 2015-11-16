#coding:utf-8
from django.db import models

class Persion(models.Model):
    name = models.CharField(max_length = 30,verbose_name = '姓名')
    gender = models.CharField(max_length = 10,verbose_name = '性别')
    age = models.IntegerField(verbose_name = '年龄')

    def __unicode__(self):
        return self.name

class Phone(models.Model):
    phone_number = models.CharField(max_length = 30,verbose_name = '电话号码')
    persion = models.ForeignKey(Persion)

#利用一对多的关系坐主外键（在子类里），如：拥有人和手机号，母亲和子女
# Create your models here.
