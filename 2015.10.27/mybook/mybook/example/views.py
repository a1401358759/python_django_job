from django.shortcuts import render_to_response

def my_view(request,month,day):
    if month == 'may' and day == '01':
        a = 'happy birthday to you young'
    return render_to_response('my_data.html',locals())
def card(request,model):
    content = model.objects.all()
    template_name = '%s.html'%model.__name__
    return render_to_response(template_name,locals())

# Create your views here.
