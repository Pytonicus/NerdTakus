from django.urls import path
from django.conf.urls import include, url
from juegos_consola import views

urlpatterns = [
    path('', views.consolas)
]