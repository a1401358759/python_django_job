from django.conf.urls import url,include,patterns

urlpatterns = patterns('mybook.photo.views',
    (r'index','index'),
    (r'nice','nice'),
    (r'hello','hello')
)
