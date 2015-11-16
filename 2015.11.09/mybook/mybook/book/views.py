from django.shortcuts import render_to_response
from models import *
from django.db import connection

cur = connection.cursor()
def index(request):
    cont = Luxury.objects.all()
    return render_to_response('index.html',locals())

def nice(request):
    p = Person.objects.get(id = '3')
    q = Person.objects.all()
    return render_to_response('nice.html',locals())

# Create your views here.
