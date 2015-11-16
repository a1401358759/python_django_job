#coding:utf-8
from django.shortcuts import render_to_response
import datetime
def index(request):
    name = 'laowang'.upper()
    createtime = datetime.datetime.now()
    class Author:
        id = '男'
    author = Author()
    return render_to_response('index.html',locals())
# Create your views here.
