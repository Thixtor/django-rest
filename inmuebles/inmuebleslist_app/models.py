from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from user_app.models import Account

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
    avg_calificacion = models.FloatField(default=0)
    number_calificacion = models.IntegerField(default=0)
    # Creamos la clave foranea para generar la relacion con la entidad empresa
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="edificacionlist")
    created = models.DateTimeField(auto_now_add=True) # Genera la fecha de registro del campo
    
    # Creamos una funcion para indicar cual es la columna a desplegar, 
    # que represente el inmueble
    def __str__(self):
        return self.direccion
    
# Class que representa los comentarios
class Comentario(models.Model):
    comentario_user = models.ForeignKey(Account, on_delete=models.CASCADE)
    calificacion = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    texto = models.CharField(max_length=200, null=True)
    edificacion = models.ForeignKey(Edificacion, on_delete=models.CASCADE, related_name="comentarios")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.calificacion) + " " + self.edificacion.direccion