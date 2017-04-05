# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 10 15:38
# Author Yo
# Email YoLoveLife@outlook.com
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from . import views
urlpatterns = [
   url(r'^$',views.index,name='index'),
   url(r'^groupsearch/',views.groupsearch,name='groupsearch'),
   url(r'^groupmodify/',views.groupmodify,name='groupmodify'),
   url(r'^hostsearch/',views.hostsearch,name='hostsearch'),
   url(r'^softversion/',views.softversion,name='softversion'),
   url(r'^batchtomcat/',views.batchtomcat,name='batchtomcat'),
   url(r'^batchmysql/',views.batchmysql,name='batchmysql'),
   url(r'^batchredis/',views.batchredis,name='batchredis'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)