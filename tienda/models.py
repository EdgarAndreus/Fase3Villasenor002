from django.db import models
import uuid


# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    marca = models.ForeignKey('Marca', on_delete=models.SET_NULL, null=True)
    precio = models.FloatField(null=True)
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


