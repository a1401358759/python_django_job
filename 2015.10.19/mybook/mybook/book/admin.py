from django.contrib import admin
from models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ['name','author','date','price','publisher']
    search_fields = ['name','author','date']
    list_filter = ['name']
    #date_hierarchy = 'date'
    ordering = ['name']
    fields = ['name','author','date','publisher','price']
    #filter_horizontal = ['name']
    #raw_id_fields = ['name']
admin.site.register(Book,BookAdmin)

# Register your models here.