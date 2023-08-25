from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='movies-home'),
    path('movie/', views.movie, name='movies-movie'),
]