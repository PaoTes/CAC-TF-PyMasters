from django.db import models


# Create your models here.
class Productos(models.Model):
    id=models.IntegerField
    Nombre=models.CharField(max_length=100)
    Descripcion=models.CharField(max_length=200)
    Precio=models.FloatField(default=0.0)
    Marca=models.CharField(max_length=20)
    Imagen=models.CharField(max_length=200, null=True)
    