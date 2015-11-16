from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def index(request):
    tem = get_template('index.html')
    con = Context({'name':'laoliu'})
    return HttpResponse(tem.render(con))