from django.shortcuts import render_to_response
from django.template import Context
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
from models import *

def index(request):
    all_content = Article.objects.order_by('date')
    template = get_template('article_index.html')
    content = Context({'book_list':all_content})
    return HttpResponse(template.render(content))

def nice(request):
    all_content = Article.objects.order_by('date')
    template = get_template('article_index.html')
    content = Context({'book_list':all_content})
    return HttpResponse(template.render(content))

def example(request):
    dicts = {
        'app' : 'my app article',
        'user' : request.user,
        'ip_address' : request.META['REMOTE_ADDR']
    }
    return dicts

def views1(request):
    template = get_template('example.html')
    c = RequestContext(request,{'message':'I am views1'},processors = [example] )
    return HttpResponse(template.render(c))

def views2(request):
    template = get_template('example.html')
    c = RequestContext(request,{'message':'I am views2'},processors = [example] )
    return HttpResponse(template.render(c))

# Create your views here.
