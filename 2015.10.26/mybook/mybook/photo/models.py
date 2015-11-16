#coding:utf-8
from django.db import models

class Photo(models.Model):
    img = models.ImageField(upload_to = 'images',verbose_name = '图片路径')
    date = models.DateField(verbose_name = '发表时间')
    p_class = models.CharField(max_length = 30,verbose_name = '图片分类')
    introduce = models.TextField(verbose_name = '图片介绍')

# Create your models here.
