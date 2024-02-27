from rest_framework import serializers
from inmuebleslist_app.models import Inmueble

class InmuebleSerializer(serializers.ModelSerializer):
    longitud_direccion =serializers.SerializerMethodField()
    
    
    class Meta:
        model = Inmueble
        fields = "__all__" # Mostramos todos los campos
        #fields = ['id', 'pais', 'active', 'imagen'] # Mostramos los campos requeridos
        #exclude = ['id'] # Excluimos los campos que no se deben mostrar
        
    def get_longitud_direccion(self, object):
        cantidad_caracteres = len(object.direccion)
        return cantidad_caracteres
    
    def validate(self, data):
        if data['direccion'] == data['pais']:
            raise serializers.ValidationError("La dirección y el pais deben ser diferentes")
        else:
            return data
    
    def validate_imagen(self, data):
        if len(data) < 2:
            raise serializers.ValidationError("la url de la imagen es muy corta")
        else:
            return data



# Creamos una funcion que se encargue de validad la propiedad dirección
# def column_longitud(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("El valor es demasiado corto")  

# class InmuebleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField(validators=[column_longitud])
#     pais = serializers.CharField(validators=[column_longitud])
#     descripcion = serializers.CharField()
#     imagen = serializers.CharField()
#     active = serializers.BooleanField()
    
#     # Creamos una funcion para crear nuevos datos
#     def create(self, validated_data):
#         # Retornamos un inmueble con todos los argumentos que corresponden
#         # al validated_data
#         return Inmueble.objects.create(**validated_data)
    
#     # Funcion para actualizar los datos
#     def update(self, instance, validated_data):
#         instance.direccion = validated_data.get('direccion', instance.direccion)
#         instance.pais = validated_data.get('pais', instance.pais)
#         instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#         instance.imagen = validated_data.get('imagen', instance.imagen)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['direccion'] == data['pais']:
#             raise serializers.ValidationError("La dirección y el pais deben ser diferentes")
#         else:
#             return data
    
#     def validate_imagen(self, data):
#         if len(data) < 2:
#             raise serializers.ValidationError("la url de la imagen es muy corta")
#         else:
#             return data
        