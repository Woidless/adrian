from django.urls import path
from . import views

from django.contrib import admin
from django.contrib.auth.views import LoginView

urlpatterns = [
    # регистрация
    path('register/', views.RegistrationView.as_view()),
    path('activate/<uuid:activation_code>/', views.ActivationView.as_view()),
    # логин и логаут
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),


    # 6
    path('', views.index),
]