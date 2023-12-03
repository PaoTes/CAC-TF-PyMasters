from django.db import models


# Create your models here.
class Productos(models.Model):
    id=models.IntegerField
    Nombre=models.CharField(max_length=100)
    Descripcion=models.CharField(max_length=200)
    Precio=models.FloatField
    Marca=models.CharField(max_length=20)