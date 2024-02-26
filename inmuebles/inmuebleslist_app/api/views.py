from inmuebleslist_app.models import Inmueble
from inmuebleslist_app.api.serializers import InmuebleSerializer
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

class InmuebleListAV(APIView):
    
    # Metodo que representa la consulta de todos los inmuebles 
    def get(self, request):
        inmuebles = Inmueble.objects.all()
        serializer = InmuebleSerializer(inmuebles, many=True)
        return Response(serializer.data)
    
    # Metodo para anadir un nuevo inmueble
    def post(self, request):
        serializer = InmuebleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class InmuebleDetalleAV(APIView):

    # Metodo para buscar un inmueble
    def get(self, request, pk):
        # Verificamos si el inmueble existe
        try:
            inmueble = Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response({'error': 'Inmueble no encontrado'},status=status.HTTP_404_NOT_FOUND)
       
        serializer = InmuebleSerializer(inmueble)
        return Response(serializer.data)
    
    # Metodo para actualizar un inmueble
    def put(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response({'error': 'Inmueble no encontrado'},status=status.HTTP_404_NOT_FOUND)
    
        serializer = InmuebleSerializer(inmueble, data=request.data)
        
        # Verificamos si la data es correcta
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Metodo para eliminar un inmueble
    def delete(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response({'error': 'Inmueble no encontrado'},status=status.HTTP_404_NOT_FOUND)
        
        # Eliminamos los datos
        inmueble.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        




# @api_view(['GET', 'POST'])
# def inmueble_list(request):
#     if request.method == 'GET':
#         inmuebles = Inmueble.objects.all()
#         serializer = InmuebleSerializer(inmuebles, many=True)
#         return Response(serializer.data)
       
        
#     if request.method == 'POST':
#         de_serializer = InmuebleSerializer(data = request.data)
        
#         # Verificamos si la data es correcta
#         if de_serializer.is_valid():
#             # Agregamos a la base de datos
#             de_serializer.save()
#             # Devolvemos el objeto agregado
#             return Response(de_serializer.data)
#         else:
#             # Devolvemos error si la data no es correcta
#             return Response(de_serializer.errors)
        
# @api_view(['GET', 'PUT', 'DELETE'])
# def inmueble_detalle(request, pk):
#     if request.method == 'GET':
#         try:
#             inmueble = Inmueble.objects.get(pk=pk)
#             serializer = InmuebleSerializer(inmueble)
#             return Response(serializer.data)
#         except Inmueble.DoesNotExist:
#                 return Response({'Error': 'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT': 
#         inmueble = Inmueble.objects.get(pk=pk)
#         de_serializer = InmuebleSerializer(inmueble, data = request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         try:
#             inmueble = Inmueble.objects.get(pk=pk)
#             inmueble.delete()
#         except Inmueble.DoesNotExist:
#             return Response({'Error': 'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)
        
#         return Response(status=status.HTTP_204_NO_CONTENT)