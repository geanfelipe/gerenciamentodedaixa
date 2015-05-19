# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from caixa import views

urlpatterns = patterns('',
    url(r'^$', views.caixa,name='caixa'),

)