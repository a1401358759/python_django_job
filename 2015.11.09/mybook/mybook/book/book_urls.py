from django.conf.urls import url,include,patterns

urlpatterns = patterns('mybook.book.views',
    (r'index','index'),
    (r'nice','nice'),
)
