from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import (login_user,dashboard,logout_user,
                    register,edit)

urlpatterns = [path('login',login_user,name ='login'),
                path('login',auth_views.LoginView.as_view(), name = 'login'),
                path('logout/',logout_user,name = 'logout'),
                path('dashboard/',dashboard,name = 'dashboard'),
                path('change-password',auth_views.PasswordChangeView.as_view(), name ='change_password'),
                path('password-change-done',auth_views.PasswordChangeDoneView.as_view(), name ='password_change_done'),
                path('register',register,name ='register'),
                path('edit/',edit,name = 'edit')]
