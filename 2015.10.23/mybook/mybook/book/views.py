#coding:utf8
from django.shortcuts import render_to_response
from models import *
from forms import *


def servers(request):
    shopping = Shop_form(initial = {'discribe': '该商品坑爹极了'}
)
    return render_to_response('shoping_server.html',locals())


# Create your views here.
