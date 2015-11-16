#coding:utf-8
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def index(request):
    tem = get_template('index.html')
    cont = Context({'name':'老王','age':12})
    return HttpResponse(tem.render(cont))

def hello(request):
    tem = get_template('index.html')
    return HttpResponse(tem.render(Context({'name':'老李'})))

def wgz(request):
    tem = get_template('wgz.html')
    new_dict = {'name':'吴广正','age':18}
    new_list = ['香蕉','桃','西瓜','菠萝','苹果',]
    cont = Context({'student':new_dict,'favorite_fruit':new_list})
    return HttpResponse(tem.render(cont))

def jj(request):
    '''
    for i in range(1,10):
	    print
	for j in range(1,i+1):
		a = '%s*%s=%s'%(j,i,i*j)
		print a.center(6),
	'''
    tem = get_template('99.html')
    num_list = range(1,10)
    cont = Context({'num_list':num_list})
    return HttpResponse(tem.render(cont))

def et(request):
    tem = get_template('et.html')
    num_list = range(1,10)
    num_list = []
    cont = Context({'num_list':num_list})
    return HttpResponse(tem.render(cont))

def flp(request):
    tem = get_template('flp.html')
    num_str = 'laobian'
    cont = Context({'num_list':num_str})
    return HttpResponse(tem.render(cont))

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