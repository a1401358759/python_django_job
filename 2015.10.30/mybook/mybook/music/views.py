from django.shortcuts import render_to_response

def index(request):
    name = 'laowang'
    name = "<script>alert('hello')</script>"

    return render_to_response('example1.html',locals())

# Create your views here.
