#coding:utf-8
from django.db import models

class StudentManager(models.Manager):
    def title_count(self,keyword):
        return self.filter(gender__icontains = keyword).count()

class Student(models.Model):
    name = models.CharField(max_length=20,verbose_name='姓名')
    gender = models.CharField(max_length=20,verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄')
    email = models.CharField(max_length=20,blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    objects = StudentManager()
# Create your models here.
