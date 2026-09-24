from django.shortcuts import render
from .models import servicio
def servicio(request):
if request.method == "POST":
Servicio = servicio(
id=request.POST["id"],
nombre=request.POST["nombre"],
precio=request.POST["precio"],
observaciones=request.POST["observaciones"],
estado=request.POST["estado"]

)
servicio.save()
return render(request, "gracias.html")
return render(request, "contacto.html")