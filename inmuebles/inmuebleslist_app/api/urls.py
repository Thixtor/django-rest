# Importamos las librerias necesarias
from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from inmuebleslist_app.api.views import inmueble_list, inmueble_detalle
from inmuebleslist_app.api.views import (EdificacionAV, EdificacionDetalleAV, EmpresaAV, EmpresaDetalleAV, 
                                         ComentarioList, ComentarioDetail, ComentarioCreate, EmpresaVS)

router = DefaultRouter()
router.register('empresa', EmpresaVS, basename='empresa')

urlpatterns = [
    path('edificacion/', EdificacionAV.as_view(), name='edificacion'),
    path('edificacion/<int:pk>', EdificacionDetalleAV.as_view(), name='edificacion-detail'),
    
    path('', include(router.urls)),
    # path('empresa/', EmpresaAV.as_view(), name='empresa'),
    # path('empresa/<int:pk>', EmpresaDetalleAV.as_view(), name='empresa-detail'),
    
    path('edificacion/<int:pk>/comentario-create/', ComentarioCreate.as_view(), name='comentario-create'),
    path('edificacion/<int:pk>/comentario/', ComentarioList.as_view(), name='comentario-list'),
    path('edificacion/comentario/<int:pk>', ComentarioDetail.as_view(), name='comentario-detail'),
    
]