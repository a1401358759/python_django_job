from django.contrib import admin
from models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','date','hot']

admin.site.register(Article,ArticleAdmin)
# Register your models here.
