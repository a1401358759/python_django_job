from django.conf.urls import patterns, include, url
from django.contrib import admin
#from book.views import *
#from photo.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mybook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #(r'hello',hello),
    #(r'hi',hi),
    #(r'hello','mybook.photo.views.hello'),
    #(r'hi','mybook.book.views.hi'),
    #(r'hello$','hello'),
    #(r'hello/(?P<name>\w+)','hello_name')

)
urlpatterns += patterns('mybook.book.views',
    (r'hi','hi'),
    (r'article_list/(?P<num>\d{1,2})','article_list'),
    (r'article_list/(?P<title>\w+)','article_content')
)
urlpatterns += patterns('mybook.photo.views',
    (r'hello$','hello'),
    (r'hello/(?P<name>\w+)','hello_name'),
)
