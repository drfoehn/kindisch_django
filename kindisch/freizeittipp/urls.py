"""kindisch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

"""

from django.conf.urls import url
from django.urls import path, include
from freizeittipp import views

urlpatterns = [
    path('freizeittipps/', views.freizeittipps, name='freizeittipps'),
    path('freizeittipp_add/', views.freizeittipp_add, name='freizeittipp_add'),
    path('freizeittipp_detail/<int:id>', views.freizeittipp_detail, name='freizeittipp_detail'),
]
