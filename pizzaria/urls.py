from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import caixa.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pizzaria.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', caixa.views.hello,name='home'),
    url(r'^caixa/', include('caixa.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )