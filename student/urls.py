from django.conf.urls import url,include
from django.contrib import admin

from student.views import qry,ppro,ppro1,upage,connect_to_tutor,like_tutor,dislike_tutor

from django.contrib.auth import views as auth_views

import views

urlpatterns = [
    url(r'^viewtutors/$',qry,name='qry'),
    url(r'^tutorprofile/(?P<expp>\d+)/$', ppro, name="ppro"),
    url(r'^buy/(?P<expp>\d+)/$',ppro1,{'tname':'buy.html'},name="buy"),
    url('^userpage',upage.as_view(),{"tname":"upage.html"},name="upage"),
    url('^upage1/',upage.as_view(),{"tname":"upage1.html"},name="upage1"),
    url('^like/$',like_tutor,name="like_tutor"),
    url('^dislike/$',dislike_tutor,name="dislike_tutor"),
    url('^connect/$',connect_to_tutor,name="connect_to_tutor")

   

   

    ]