# -*- coding:utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maintain.views.home', name='home'),
    # url(r'^maintain/', include('maintain.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #host info
    #nagios客户端访问API接口地址
    url(r'^api/gethosts\.json$','hostinfo.views.gethosts'),
    #客户端访问API进行上传数据的API
    url(r'^api/collect$','hostinfo.views.collect'),
    
)
