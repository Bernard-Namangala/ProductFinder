"""
authentication urls
"""

# app_name = "authentication"

from django.urls import path, include
from . import views
from .forms import EmailValidationOnForgotPassword
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(form_class=EmailValidationOnForgotPassword), 
         name='password_reset'),
    path('', include("django.contrib.auth.urls")),
    path('register/', views.register, name="register"),
    path('<int:pk>/', views.ProfileView.as_view(), name="profile"),
    path('edit-email/', views.edit_email_view, name="edit_email")
]