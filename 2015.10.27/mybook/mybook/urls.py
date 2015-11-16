from django.conf.urls import patterns, include, url
from django.contrib import admin
from example.models import Student,Teacher
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mybook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
example = patterns('mybook.example.views',
    (r'mybirthday','my_view',{'month':'may','day':'01'}),
    (r'mydate/(?P<month>\w+)/(?P<day>\d{1,2})$','my_view'),
    (r'student_card','card',{'model':Student}),
    (r'teacher_card','card',{'model':Teacher})
)
urlpatterns += example