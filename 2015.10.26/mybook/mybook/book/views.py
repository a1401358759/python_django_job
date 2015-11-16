from django.shortcuts import render_to_response
from models import *
def hi(request):
    return render_to_response('hi_world.html')

def article_list(request,num):
    num = int(num)
    content = Article.objects.order_by('id')
    content1 = content[(int(num)-1)*5:int(num)*5]
    lens = range(1,len(content)/5+1)
    return render_to_response('article_list.html',locals())

def article_content(request,title):
    article = Article.objects.get(atricle_src = title)
    return render_to_response('article_content.html',locals())
# Create your views here.
