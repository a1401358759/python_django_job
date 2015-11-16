from django.contrib import admin
from models import *
class LuxuryAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','brand']

class PersionAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name']

admin.site.register(Luxury,LuxuryAdmin)
admin.site.register(Person,PersionAdmin)

# Register your models here.
