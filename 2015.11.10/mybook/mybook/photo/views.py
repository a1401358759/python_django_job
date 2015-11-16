from django.shortcuts import render_to_response

def index(request,phone):
    return render_to_response('photo_index.html',locals())

def nice(request,phone):
    return render_to_response('photo_nice.html',locals())

def hello(request,phone):
    return render_to_response('photo_hello.html',locals())

# Create your views here.
