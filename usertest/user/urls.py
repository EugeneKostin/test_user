"""usertest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.UserRegistrationForm, name='registration'),
	path('logout/', views.logout_user, name='logout'),
	path('login/', views.login_user, name='login'),
    path('keylogin/', views.UserRegistrationForm, name='keylogin'),
    path('reppassword/',views.forgotPassword, name='reppassword'),
    path('passwordreq/',views.passwordRecovery, name='passwordreq'),
    path('edit/', views.edit_user, name='edit'),
    path('delete/', views.delete_user, name='delete'),
]
