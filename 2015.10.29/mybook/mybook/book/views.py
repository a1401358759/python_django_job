from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html',locals())
def jianjie(request):
    return render_to_response('jianjie.html',locals())
def news(request):
    return render_to_response('new.html',locals())
def show(request):
    return render_to_response('show.html',locals())
def order(request):
    return render_to_response('order.html',locals())
def phone(request):
    return render_to_response('phone.html',locals())
def gyl(request):
    return render_to_response('gyl.html',locals())
def xs(request):
    return render_to_response('xs.html',locals())

# Create your views here.
