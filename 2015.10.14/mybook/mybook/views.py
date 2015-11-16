#coding:utf-8
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template


def dh(request):
    tem = get_template('dh.html')
    dh_list = [
        '首页',
        '产品介绍',
        '公司新闻',
        '关于我们',
        '网上订购'
    ]
    cont = Context({'dh_list':dh_list})
    return HttpResponse(tem.render(cont))
def city(request):
    tem = get_template('city.html')
    country = {
        '中国':['北京','张家口','保定','石家庄','涿州','定州','霸州'],
        '日本':['广岛','长崎','东京','大阪','横滨','北海道','名古屋'],
        '美国':['纽约','华盛顿','芝加哥','底特律','西雅图','洛杉矶','新奥尔良']
    }
    #country = {'a':'abcde','b':'fghij'}
    cont = Context({'country':country})
    return HttpResponse(tem.render(cont))

def bj(request):
    tem = get_template('bj.html')
    cont = Context({'a':'1','b':4,'num':range(100)})
    return HttpResponse(tem.render(cont))

def glq(request):
    tem = get_template('glq.html')
    cont = Context({'lower':list('abcde'),'upper':list('abcde'.upper())})
    return HttpResponse(tem.render(cont))
from django.shortcuts import render_to_response
import time

def fb(request):
    t = time.ctime()
    name = 'laobian'
    return render_to_response('fb.html',locals())
