from django.contrib import admin
from models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','gender','age']

admin.site.register(Student,StudentAdmin)
# Register your models here.
