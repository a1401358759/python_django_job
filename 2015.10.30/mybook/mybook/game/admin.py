from django.contrib import admin
from models import *
class GameAdmin(admin.ModelAdmin):
    list_display = ['id','title','types']

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id','name','paiming']

admin.site.register(Game,GameAdmin)
admin.site.register(Player,PlayerAdmin)

# Register your models here.
