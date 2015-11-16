#coding:utf-8
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length = 50,verbose_name='书名')
    author = models.CharField(max_length = 30,verbose_name='作者',blank=True)#blank默认可以为空
    date = models.DateField(verbose_name='出版日期')
    price = models.FloatField(verbose_name='价格')
    publisher = models.CharField(max_length = 50,verbose_name='出版社')

    def __unicode__(self):
        return self.name
# Create your models here.
