from django.shortcuts import render
from .models import Mensaje

# Create your views here.

def contacto(request):
if request.method == "POST":
    mensaje = Mensaje(
        nombre=request.POST["nombre"],  #Capturar el valor de la caja de texto nombre
        correo=request.POST["correo"],  #Capturar el valor de la caja de texto correo
        mensaje=request.POST["mensaje"] #Capturar el valor de la caja de texto mensaje
    )
    mensaje.save()  #Guarda en la base de datos
    return render(request, "gracias.html")
    return render(request, "contacto.html")