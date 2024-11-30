
from django.urls import path , include
from .views import *

urlpatterns = [

    path('',user_profile, name="user_profile"),
    path('profile_edit/',profile_edit, name="profile_edit"),
    path('change_pass/',change_pass, name="change_pass"),

]