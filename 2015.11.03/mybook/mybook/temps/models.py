from django.db import models

class Persion(models.Model):
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    gender = models.CharField(max_length = 20)
# Create your models here.
