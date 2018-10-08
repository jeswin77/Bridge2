from django.conf.urls import url,include
from django.contrib import admin

from tutor.views import upload_file,notes,search,ad

from django.contrib.auth import views as auth_views

import views

urlpatterns = [
    url(r'^tutornotes/$',upload_file,name='upload_file'),
    url(r'^viewnotes/$',notes,name="notes"),
    url(r'^addad/$',ad,name="ad")

    
  
   

   

    ]