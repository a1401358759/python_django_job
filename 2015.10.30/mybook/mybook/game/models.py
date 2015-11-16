#coding:utf-8
from django.db import models

class Game(models.Model):
    title = models.CharField(max_length = 30,verbose_name = '游戏名称')
    types = models.CharField(max_length = 30,verbose_name = '游戏类型')
    date = models.DateField(verbose_name = '发布日期')
    company = models.CharField(max_length= 50,verbose_name = '发布公司')
    dx = models.FloatField(verbose_name = '游戏大小')
    introduction = models.TextField(verbose_name = '游戏简介')
    image = models.ImageField(upload_to = 'game/static/images',verbose_name= '游戏图片')

class Player(models.Model):
    name = models.CharField(max_length = 30,verbose_name = '玩家姓名')
    gender = models.CharField(max_length = 4,verbose_name = '性别')
    paiming = models.CharField(max_length = 10,verbose_name = '玩家等级' )
# Create your models here.







