from django.contrib import admin
from models import *

class PersionAdmin(admin.ModelAdmin):
    list_display = ['id','name','age']

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id','phone_number']

admin.site.register(Persion,PersionAdmin)
admin.site.register(Phone,PhoneAdmin)

# Register your models here.
