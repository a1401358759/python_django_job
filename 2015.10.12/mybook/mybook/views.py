from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def index(request):
    tem = get_template('index.html')
    content = Context({'name':'laobian'})
    return HttpResponse(tem.render(content))


'''
import time

def times(request):
    return HttpResponse(time.ctime())

def hi(request,num):
    return HttpResponse(num)
'''