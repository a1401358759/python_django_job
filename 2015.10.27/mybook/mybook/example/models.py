#coding:utf-8
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.CharField(max_length=10,verbose_name='年龄')
    grade = models.CharField(max_length=10,verbose_name='年级')
    address = models.CharField(max_length=30,verbose_name='住址')
    photo = models.ImageField(upload_to='images/s/photo',verbose_name='相片')

class Teacher(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.CharField(max_length=10,verbose_name='年龄')
    project = models.CharField(max_length=10,verbose_name='科目')
    address = models.CharField(max_length=30,verbose_name='住址')
    photo = models.ImageField(upload_to='images/s/photo',verbose_name='相片')
# Create your models here.
