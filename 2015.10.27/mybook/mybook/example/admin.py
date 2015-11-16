from django.contrib import admin
from models import Student,Teacher

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','grade']

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','project']

admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
# Register your models here.
