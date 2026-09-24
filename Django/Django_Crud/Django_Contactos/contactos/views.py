from django.shortcuts import render
from .models import Contacto

def crear(request):
    if request.method == 'POST':
        contacto = Contacto(
            nombre = request.POST["nombre"],
            correo = request.POST["correo"],
            telefono = request.POST["telefono"],
            mensaje = request.POST["mensaje"]
        )
        contacto.save()
    return render(request, "formulario.html")
def listar(request):
    #trae todos los registrados de la tabla contactos. #Select * from contactos
    contactos = Contacto.objects.all()
    return render(
        request, 
        "listado.html", 
        {"contactos": contactos}
    )