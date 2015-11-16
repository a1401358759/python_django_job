from django.contrib import admin
from models import *

class ArticleAddmin(admin.ModelAdmin):
    list_display = ['id','title','author']

admin.site.register(Article,ArticleAddmin)

# Register your models here.
