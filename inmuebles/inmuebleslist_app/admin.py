from django.contrib import admin
from inmuebleslist_app.models import Edificacion, Empresa
# Register your models here.
# Para agregar la estructura a nuestra aplicación

admin.site.register(Edificacion)
admin.site.register(Empresa)