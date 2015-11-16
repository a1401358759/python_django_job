from django.conf.urls import patterns, include, url

urlpatterns = patterns('mybook.article.views',
    (r'index','index'),
    (r'nice','nice'),
    (r'example','example'),
    (r'views1','views1'),
    (r'views2','views2')

)