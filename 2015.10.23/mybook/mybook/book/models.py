from django.db import models

class Shopping(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    date = models.DateField()
    address = models.CharField(max_length=50)
    expiration_time = models.IntegerField()

class Ding_form(models.Model):
    adress = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    all_price = models.FloatField()

class Buy(models.Model):
    shopping_id = models.IntegerField()
    shoping_number = models.IntegerField()
    shoping_price = models.FloatField()
    Ding_id = models.IntegerField()

class Img(models.Model):
    img = models.ImageField(upload_to='img')
# Create your models here.
