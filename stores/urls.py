"""
store app urls
"""

from django.urls import path
from . import views
urlpatterns = [
    path('<slug:store_name>/', views.storeview, name="store")
]