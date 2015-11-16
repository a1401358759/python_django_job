from django.shortcuts import render_to_response

def index(request):
    title = 'index'
    return render_to_response('index.html',locals())

def includes(request):
    title = 'include'
    incl = 'index.html'
    return render_to_response('includes.html',locals())


def base(request):
    return render_to_response('base.html')

def show(request):
    return render_to_response('show.html')
