from django.db import models

# Create your models here.

# Class para administrar empresa
class Empresa(models.Model):
    nombre = models.CharField(max_length=250)
    website = models.URLField(max_length=250) # Tipo de dato para websites
    active = models.BooleanField(default=True)
    
    # Creamos una funcion para desplegar la informacion de la empresa en el
    # dashwork de Django
    def __str__(self):
        return self.nombre

# Class que representa el imbueble
class Edificacion(models.Model):
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=900)
    active = models.BooleanField(default=True)
    # Creamos la clave foranea para generar la relacion con la entidad empresa
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="edificacion")
    created = models.DateTimeField(auto_now_add=True) # Genera la fecha de registro del campo
    
    # Creamos una funcion para indicar cual es la columna a desplegar, 
    # que represente el inmueble
    def __str__(self):
        return self.direccion
    

    
    