from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=5)
    age = models.IntegerField()
    grade = models.IntegerField()
    phone = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

# Create your models here.
