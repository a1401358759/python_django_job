from django.conf.urls import patterns, include, url
from django.contrib import admin
from book.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mybook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'book',book_hot)
)

