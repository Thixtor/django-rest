from rest_framework import serializers
from inmuebleslist_app.models import Inmueble

class InmuebleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    direccion = serializers.CharField()
    pais = serializers.CharField()
    descripcion = serializers.CharField()
    imagen = serializers.CharField()
    active = serializers.BooleanField()
    
    # Creamos una funcion para crear nuevos datos
    def create(self, validated_data):
        # Retornamos un inmueble con todos los argumentos que corresponden
        # al validated_data
        return Inmueble.objects.create(**validated_data)
    
    # Funcion para actualizar los datos
    def update(self, instance, validated_data):
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.pais = validated_data.get('pais', instance.pais)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance