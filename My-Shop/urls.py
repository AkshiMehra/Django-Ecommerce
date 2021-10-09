from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

app_name = "myshop"
urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('checkout/', views.checkout, name = "checkout")
]
