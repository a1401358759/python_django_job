from django.contrib import admin
from models import *

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','p_class','date']

admin.site.register(Photo,PhotoAdmin)
# Register your models here.
