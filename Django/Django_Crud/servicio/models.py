from django.db import models
class servicio(models.Model):
id_servicio = models.BigAutoField(primary_key=True)
nombre = models.CharField(max_length=100)
precio = models.IntergerField(max_digits=10)
observaciones = models.TextField()
estado = models.BooleanField()