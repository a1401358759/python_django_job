from django.conf.urls import patterns, include, url

urlpatterns = patterns('mybook.book.views',
    (r'index','index'),
    (r'frame','frame'),
    (r'input','form_input'),
    (r'output','form_output')
)