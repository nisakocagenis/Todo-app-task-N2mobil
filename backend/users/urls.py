from django.contrib import admin
from django.urls import path
from .views import all_users

urlpatterns = [
    path("", all_users, name="user"),
    
]