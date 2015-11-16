from django.shortcuts import render_to_response
from models import *


def book_hot(request):
    book_list = Book.objects.order_by('-date')
    return render_to_response('book.html',locals())
# Create your views here.