from django.shortcuts import render
from .models import Mensaje

# Create your views here.
def clientes(request):
    if request.method == "POST":
        mensaje = Mensaje(
            id = request.POST["id"],
            numero_documento = request.POST["numero_documento"],
            nombre = request.POST["nombre"],
            apellidos = request.POST["apellidos"],
            direccion = request.POST["direccion"],
            email = request.POST["email"],            
            mensaje=request.POST["mensaje"]
        )