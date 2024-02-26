from django.db import models

# Create your models here.

# Creamos la clase que represente un inmueble
class Inmueble(models.Model):
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=900)
    active = models.BooleanField(default=True)
    
    # Creamos una funcion para indicar cual es la columna a desplegar, 
    # que represente el inmueble
    def __str__(self):
        return self.direccion
    
    