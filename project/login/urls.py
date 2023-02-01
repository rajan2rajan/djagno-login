from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signuppage , name='signup'),
    path('login/',views.loginpage , name='login'),
    path('home/',views.homepage , name='home'),
    path('logout/',views.logoutpage , name='logout'),
    path('changepassword/',views.changepasswordpage , name='changepassword'),

]
