from django.conf.urls import patterns, include, url
from controle import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pizzaria.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.hello,name='home'),

)