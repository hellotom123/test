# -*- coding: utf-8 -*-

from django.conf.urls import patterns
# from  home_application import chaxun_redis
urlpatterns = patterns('home_application.views',
    (r'^$', 'home'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
    (r'^compute/$','compute'),
    # (r'^redis/redis-online.html$','redis_online'),
    # (r'^redis/$',chaxun_redis.select),
)
