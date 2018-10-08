from django.conf.urls import url,include
from django.contrib import admin

from log.views import RegisterStudent,userselect,CourseSelect,RegisterTutor,Profile,EditProfile,ChangePassword,TutorUpdate,StudentUpdate
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import password_reset,password_reset_done,password_reset_confirm,password_reset_complete
from tutor.views import search
import views

urlpatterns = [
    
    url('^logs/',RegisterStudent.as_view(),name="log"),
    url('^logt/',RegisterTutor.as_view(),name="log"),
    url('^login/', auth_views.login, {'template_name': 'log.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^profile/',Profile,name="profile"),
    url(r'^search/$',search,name="search"),
    url(r'^editprofile/',EditProfile.as_view(),name="editprofile"),
    url(r'^editprofiletutor',TutorUpdate.as_view(),name="EditProfileTut"),
    url(r'^editprofilestudent',StudentUpdate.as_view(),name="EditProfilestud"),
    url(r'^changepassword/$',ChangePassword,name="changepassword"),
    url(r'^userselect',userselect.as_view(),name="userselect"),
    url(r'^courseselect/',CourseSelect.as_view(),name="courseselect"),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url('^', include('django.contrib.auth.urls'))
    ]
