from django.contrib import admin
from models import *

class ShoppingAdmin(admin.ModelAdmin):
    list_display = ['id','name','price']
class Ding_formAdmin(admin.ModelAdmin):
    list_display = ['id','phone','adress']
class BuyAdmin(admin.ModelAdmin):
    list_display = ['id','Ding_id',]
class ImgAdmin(admin.ModelAdmin):
    list_display = ['id','img',]

admin.site.register(Shopping,ShoppingAdmin)
admin.site.register(Ding_form,Ding_formAdmin)
admin.site.register(Buy,BuyAdmin)
admin.site.register(Img,ImgAdmin)

# Register your models here.
