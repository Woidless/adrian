from django.urls import path
from . import views


urlpatterns = [
    # регистрация
    path('register/', views.RegistrationView.as_view()),
    path('activate/<uuid:activation_code>/', views.ActivationView.as_view()),
    # логин и логаут
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
]