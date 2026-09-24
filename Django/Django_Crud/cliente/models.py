from django.db import models
class servicio(models.Model):
id_cliente = models.BigAutoField(primary_key=True)
numero_documento = models.CharField(max_length=10)
nombre = models.CharField(max_length=50)
apellidos = models.CharField(max_length=50)
direccion = models.CharField(max_length=100)
correo = models.EmailField(max_length=50)
