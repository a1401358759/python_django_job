#coding:utf-8
from django.db import models

class Mother(models.Model):
    name = models.CharField(max_length = 30, verbose_name = '姓名')
    age = models.IntegerField(verbose_name = '年龄')
    photo = models.ImageField(upload_to = 'static/img/mother',verbose_name = '照片')
    def __unicode__(self):
        return self.name

class Child(models.Model):
    name = models.CharField(max_length = 30, verbose_name = '姓名')
    age = models.IntegerField(verbose_name = '年龄')
    photo = models.ImageField(upload_to = 'static/img/child',verbose_name = '照片')
    mother = models.ForeignKey(Mother)

class Teacher(models.Model):
    name = models.CharField(max_length = 30, verbose_name = '姓名')
    age = models.IntegerField(verbose_name = '年龄')
    photo = models.ImageField(upload_to = 'static/img/teacher',verbose_name = '照片')
    def __unicode__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length = 30, verbose_name = '姓名')
    age = models.IntegerField(verbose_name = '年龄')
    photo = models.ImageField(upload_to = 'static/img/student',verbose_name = '照片')
    teacher =  models.ManyToManyField(Teacher)
    def __unicode__(self):
        return self.name





# Create your models here.
