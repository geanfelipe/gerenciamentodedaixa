from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import controle.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pizzaria.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', controle.views.hello,name='home'),
    url(r'^$', include('controle.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )