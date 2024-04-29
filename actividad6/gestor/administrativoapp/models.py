from django.db import models

class TuModelo(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.IntegerField()
    Direccion = models.BooleanField()

