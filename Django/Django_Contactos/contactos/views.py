from django.shortcuts import render

from .models import Contacto


def crear(request):
    if request.method == 'POST':
        Contacto.objects.create(
            nombre=request.POST.get('nombre', '').strip(),
            correo=request.POST.get('correo', '').strip(),
            telefono=request.POST.get('telefono', '').strip(),
            mensaje=request.POST.get('mensaje', '').strip(),
        )

    return render(request, 'formulario.html')


def listar(request):
    contactos = Contacto.objects.all()
    return render(request, 'lista.html', {'contactos': contactos})
