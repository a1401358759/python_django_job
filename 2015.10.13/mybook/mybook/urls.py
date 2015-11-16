from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mybook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^index$',index),
    (r'hello',hello),
    (r'student',wgz),
    (r'\d{2}',jj),
    (r'et',et),
    (r'flp',flp),
    (r'dh',dh)
)
