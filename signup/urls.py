"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path ,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('indexing',views.index,name='index'),
    path('acccess_sess',views.acccess_sess,name='acccess_sess'),
    path('delete_sess',views.delete_sess,name='delete_sess'),
    path('signup',views.Signup,name='Signup'),
    path('account_activation_sent',views.account_activation_sent,name='account_activation_sent'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    path('',views.user_log,name='user_log'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='passwordreset.html'),name='reset_password'),

   # path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset_done'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'),name='password_reset_done'),

    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='passwordreset_form.html'),name= 'password_reset_confirm'),
    #path(auth_views.PasswordResetDoneView)
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'),name='password_reset_compelte'),

]
