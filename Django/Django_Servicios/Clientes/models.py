from django.db import models

# Create your models here.
class Clientes(models.Model):
    id = models.BigAutoField(primary_key=True)
    numero_documento = models.IntegerField()
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=60)
    direccion = models.TextField(max_length=30)
    email = models.EmailField()