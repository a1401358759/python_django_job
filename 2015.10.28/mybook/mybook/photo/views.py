from django.shortcuts import render_to_response

def index(request):
    return render_to_response('photo_index.html',locals())

# Create your views here.
