"""URL configuration for the contact project."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactos/', include('contactos.urls')),
]
