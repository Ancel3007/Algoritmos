from django.http import HttpResponse #Libreria para recibir respuestas http

def home(request):
    return HttpResponse("Hello guys")