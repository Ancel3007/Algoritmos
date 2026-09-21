from django.shortcuts import render
from .models import Mensaje

# Create your views here.
def servicios(request):
    if request.method == "POST":
        mensaje = Mensaje(
            id = request.POST["id"],
            nombre = request.POST["nombre"],
            precio = request.POST["precio"],
            observaciones = request.POST["observaciones"],
            estado = request.POST["estado"],
            mensaje=request.POST["mensaje"]
        )