from django.urls import path

from . import views

urlpatterns = [
    path('', views.crear, name='crear_contacto'),
    path('lista/', views.listar, name='lista_contactos'),
]
