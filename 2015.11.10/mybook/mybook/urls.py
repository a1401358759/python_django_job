from django.conf.urls import patterns, include, url
from django.contrib import admin
from book.models import *

gmm = Persion.objects.get(id = 2)
xtl = Persion.objects.get(id = 1)
gm_phone = gmm.phone_set.all()
xt_phone = xtl.phone_set.all()
phone_number = {
    'phone':{
        'gmm':gmm,
        'xtl':xtl,
        'gm_phone':gm_phone,
        'xt_phone':xt_phone
    }
}

urlpatterns = patterns('mybook.book.views',
    # Examples:
    # url(r'^$', 'mybook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^photo/',include('mybook.photo.photo_urls'),phone_number),
    (r'index','index'),
    (r'indet','indet',{'page':'index.html'}),
    (r'indev/(\w+)','indev'),
    (r'phone','phone',phone_number)

)
