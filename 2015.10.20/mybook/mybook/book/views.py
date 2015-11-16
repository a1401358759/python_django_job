#coding:utf-8
from django.shortcuts import render_to_response

def bd(request):
    return render_to_response('bd.html',locals())
def lianxi(request):
    age_list = range(18,51)
    #edu_list = '见习法师 初级法师 中级法师 高级法师 大法师 魔导士 魔导师 大魔导师 圣魔导师 法神'.split()
    bl = '法师'.decode('utf8')
    tjl = request.GET.get('major')

    if 'major' in request.GET and request.GET['major']:
        if request.GET['major'] == '法师'.decode('utf8'):
            edu_list = '见习法师 初级法师 中级法师 高级法师 大法师 魔导士 魔导师 大魔导师 圣魔导师 法神'.split()
        elif request.GET['major'] == '学生'.decode('utf8'):
            edu_list = '小学 初中 高中 中专 大专 本科 研究生 博士'.split()

    return render_to_response('lianxi.html',locals())
def myreq(request):
    return render_to_response('req.html',locals())

def sjk(request):

    "content = Major.objects.filter(major = '%s'%request.GET['major'])"
    pass
from models import *
def filters(request):
    filters = Book.objects.filter(price = 0,date = '2015-10-28')
    return render_to_response('filters.html',locals())
# Create your views here.
