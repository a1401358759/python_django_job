from django.shortcuts import render_to_response

def index(request):
    name = '''
    <script>
        alert('hello world')
    </script>
    '''
    return render_to_response('index.html', locals())
def frame(request):
    return render_to_response('frames.html', locals())

def form_input(request):
    return render_to_response('form_input.html',locals())

def form_output(request):
    return render_to_response('form_output.html',locals())
# Create your views here.
