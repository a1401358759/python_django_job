from django.conf.urls import patterns, include, url
from django.contrib import admin
from school.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myschool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'index',index),
    (r'show',show)
)
