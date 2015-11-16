#coding:utf-8
from django.shortcuts import render_to_response
from models import *
def index(request):
    a = Student.objects.title_count('男')
    b = Student.objects.all()
    return render_to_response('index.html',locals())
# Create your views here.
