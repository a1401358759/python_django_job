from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s:%s'%(self.id,self.name)
    class Meta:
        ordering = ['name']
# Create your models here.
