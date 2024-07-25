from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('sdsfsdfsdf/', views.register, name='register'),
    path('gsdsdfdgfbfdgfd/', views.login, name='login'),
    path('hrtryfghfghfgh/', views.dashboard, name='dashboard'),
    path('ldrtfgio/', views.logout, name='logout'),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
]