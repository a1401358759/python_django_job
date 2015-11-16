from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'statics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'index',index),
    (r'^jianjie.html$',jianjie),
    (r'^new.html$',news),
    (r'^show.html',show),
    (r'^order.html',order),
    (r'^phone.html',phone),
    (r'^gyl.html',gyl),
    (r'^xs.html',xs)
)
