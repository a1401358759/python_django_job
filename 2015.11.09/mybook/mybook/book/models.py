#coding:utf-8
from django.db import models

class LuxuryManager(models.Manager):
    def get_queryset(self):
        return super(LuxuryManager,self).get_queryset().filter(price = 38)



class Luxury(models.Model):
    name = models.CharField(max_length = 50, verbose_name = '名称')
    price = models.IntegerField(verbose_name = '价格')
    photo = models.ImageField(upload_to = 'images',verbose_name = '图片')
    brand = models.CharField(max_length = 50, verbose_name = '品牌')

    objects = models.Manager()
    Luxury_objects = LuxuryManager()


class Person(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    birth_date = models.DateField()
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 100)

    def baby_boomer_status(self):
        import datetime
        if datetime.date(1945, 8, 1) <= self.birth_date <= datetime.date(1964, 12, 31):
            return "Baby boomer"
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        return "Post-boomer"

    def is_midwestern(self):
        return self.state in ('IL', 'WI', 'MI', 'IN', 'OH', 'IA', 'MO')

    def _get_full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)

from django.db import connection, models

class PersonManager(models.Manager):
    def first_names(self, last_name):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT DISTINCT first_name
            FROM people_person
            WHERE last_name = %s""", [last_name])
        return [row[0] for row in cursor.fetchone()]

class Persons(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    obj = PersonManager()


# Create your models here.
