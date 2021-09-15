from django.urls import path
from .views import *

urlpatterns=[
    path('register/', userRegistartion, name='userregister'),
    path('login/', userLogin, name='userLogin'),
    path('logout/', userLogout, name='userlogout'),
    path('profile/', userProfile, name='userprofile'),
    path('editprofile/', editprofile, name='editprofile')
]