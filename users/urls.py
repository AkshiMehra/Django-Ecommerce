from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
]
