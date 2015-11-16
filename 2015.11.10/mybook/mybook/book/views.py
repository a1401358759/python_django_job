from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html',locals())

def indet(request,page):
    return render_to_response(page,locals())

def indev(request,page):
    return render_to_response('%s.html'%page,locals())

def phone(request,phone):
    return render_to_response('phone.html',locals())
# Create your views here.
