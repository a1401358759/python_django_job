from django.shortcuts import render_to_response
from models import *

def index(request):
    eldest_daughter = Child.objects.get(id = 1)
    moth = eldest_daughter.mother
    age = moth.age
    return render_to_response('index.html',locals())

def childs(request):
    moth = Mother.objects.get(id = 2)
    childs = moth.child_set.all()
    return render_to_response('hello.html',locals())

def mtm(request):
    b = Student.objects.get(id = 2)
    c = b.teacher.all()

    t = Teacher.objects.get(id = 2)
    s = t.student_set.all()
    return render_to_response('mtm.html',locals())

# Create your views here.
