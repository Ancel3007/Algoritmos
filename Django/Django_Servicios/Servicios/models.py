from django.db import models

# Create your models here.
class Servicios(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    observaciones = models.TextField(max_length=255)
    estado = models.BooleanField()