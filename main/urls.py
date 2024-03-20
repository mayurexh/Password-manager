from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import (displayPasswords,
                     createPassword,
                    #  singlePasswordView
)

urlpatterns = [
    path('', views.home , name="home"),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'main/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('passwords/', displayPasswords.as_view(), name ='passwords'),
    path('newpassword/', createPassword.as_view(), name="newpassword"),
    path('passwords/<int:id>/', views.singlePasswordView, name="single_password")

]
