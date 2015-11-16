from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mybook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'article/',include('mybook.article.article_urls')),
    (r'game/',include('mybook.game.game_urls')),
    (r'music/',include('mybook.music.music_urls'))

)
