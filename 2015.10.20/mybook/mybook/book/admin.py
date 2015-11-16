from django.contrib import admin
from models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ['id','name','author','date']

admin.site.register(Book,BookAdmin)
# Register your models here.
