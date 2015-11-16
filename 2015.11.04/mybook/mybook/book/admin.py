from django.contrib import admin
from models import *

class MotherAdmin(admin.ModelAdmin):
    list_display = ['id','name','age']
class ChildAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','mother']
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','age']
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','age']

admin.site.register(Mother,MotherAdmin)
admin.site.register(Child,ChildAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)

# Register your models here.
