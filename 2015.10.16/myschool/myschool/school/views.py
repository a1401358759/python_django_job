#coding:utf-8
import random
from django.shortcuts import render_to_response
from  models import Student

def index(request):
    try:
        name = ['老王','老李','老刘','老张','老猪',]
        age = [i+20 for i in range(5)]
        gender = [random.choice(['男','女']) for i in range(5)]
        phone = ['1302222222%s'%i for i in range(5)]
        grade = [random.randint(1,5) for i in range(5)]
        values = zip(name,age,gender,phone,grade)
        for i in values:
            Student.objects.create(name = i[0], age = i[1], gender = i[2], phone = i[3],grade = i[4])
        logo = True
    except Exception,e:
        logo = False
    #news = Student.objects.create(name = '', age = , gender = '', phone = '',grade = )
    return render_to_response('index.html',locals())

def show(request):
    content = Student.objects.all()
    return render_to_response('show.html',locals())
# Create your views here.
