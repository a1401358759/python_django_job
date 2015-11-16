#coding:utf-8
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 50,verbose_name = '文章标题' )
    author = models.CharField(max_length = 30,verbose_name = '文章作者')
    content = models.TextField(verbose_name = '文章内容')
    date = models.DateField(verbose_name = '发表日期')
    img = models.ImageField(upload_to = 'article/static/images',verbose_name='文章插图')
    hot = models.IntegerField(verbose_name = '点击率')
    src = models.CharField(max_length = 70,verbose_name = '文章链接')
# Create your models here.
