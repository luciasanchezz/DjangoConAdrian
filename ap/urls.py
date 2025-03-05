from .views import *
from django.urls import path

urlpatterns = [
    path('', ListaProducto.as_view(), name='lista'),
    path('producto_detalle/<int:pk>', DetalleProducto.as_view(), name='detalle'),
    path('producto_crear', CrearProducto.as_view(), name='crea'),
    path('producto_editar/<int:pk>', EditarProducto.as_view(), name='editar'),
    path('producto_eliminar/<int:pk>', EliminarProducto.as_view(), name='eliminar'),
    path('registra', RegistraUsuario.as_view(), name='registra'),
]