from django.shortcuts import render_to_response
from models import *
from forms import *
def hello(request):
    hello = User.objects.all()
    return render_to_response('hello.html',locals())

def hi(request):
    hi = ContactForm({'subject': '1','email':'adminqq.com','message':'2'})
    t = hi['email'].errors
    return render_to_response('hi.html',locals())

# Create your views here.
