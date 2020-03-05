# -*- conding:utf-8 -*-
from django.conf.urls import url
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from .views import ShowAllHospitalInfo, ShowTokyoHospitalInfo


# 视图逻辑
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('app1/', views.index, name='index'),
    path('app1/info/', ShowAllHospitalInfo.as_view(), name='info'),
    path('app1/info/tokyo/', ShowTokyoHospitalInfo.as_view(), name='info'),
]
