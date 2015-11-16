#coding:utf-8
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=30,verbose_name='文章标题')
    atricle_src = models.CharField(max_length=50,verbose_name='文章链接')
    author = models.CharField(max_length=30,verbose_name='文章作者')
    date = models.DateField(verbose_name='发表日期')
    content = models.TextField(verbose_name='文章内容')
    img = models.ImageField(upload_to='images',verbose_name='文章图片')
# Create your models here.
