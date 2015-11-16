from django.shortcuts import render_to_response
from models import *
def hello(request):
    return render_to_response('hello_world.html')
def hello_name(request,name):
    return render_to_response('hello_world.html',locals())


# Create your views here.
