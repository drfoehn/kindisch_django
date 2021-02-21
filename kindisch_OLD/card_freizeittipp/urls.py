from django.conf.urls import url
from django.urls import path
from card_freizeittipp import views

urlpatterns = [
    path('', views.freizeittipps, name='freizeittipps'),
]
