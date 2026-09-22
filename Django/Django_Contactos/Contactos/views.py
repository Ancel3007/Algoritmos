from django.shortcuts import render
from .models import Contacto

# Create your views here.

def crear(request):
    if request.method == POST:
        contacto = Contacto(
            nombre = request.POST["nombre"]
            correo = request.POST["correo"]
            telefono = request.POST["telefono"]
            mensaje = request.POST["mensaje"]
        )

        contacto.save()
        return render(request, "contactos/formularios.html")