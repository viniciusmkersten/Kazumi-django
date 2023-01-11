from django.urls import path
from . import views

urlpatterns = [
    path('', views.primeira_pagina, name='pagina'),

]