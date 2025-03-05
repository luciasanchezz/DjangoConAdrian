from django.shortcuts import render
from .models import *
from django.views.generic import *
from .forms import *
from django.urls import reverse_lazy


# Create your views here.
class DetalleProducto(DetailView):
    model = Producto
    template_name = 'ap/producto_detalle.html'
    context_object_name = 'producto'

class CrearProducto(CreateView):
    model = Producto
    template_name = 'ap/producto_crear.html'
    form_class = CreaProducto
    success_url = reverse_lazy('lista') #se pone el name de las url

class EditarProducto(UpdateView):
    model = Producto
    template_name = 'ap/producto_editar.html'
    form_class = CreaProducto
    success_url = reverse_lazy('lista')

class EliminarProducto(DeleteView):
    model = Producto
    template_name = 'ap/producto_eliminar.html'
    context_object_name = 'producto'
    success_url = reverse_lazy('lista')

class ListaProducto(ListView):
    model = Producto
    template_name = 'ap/producto.html'
    context_object_name = 'productos'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['marcas'] = Marca.objects.all()
        return contexto
        
    def get_queryset(self):
        query = super().get_queryset()
        filtro_categoria = self.request.GET.get('filtro_categoria')
        filtro_marca = self.request.GET.get('filtro_marca')

        if filtro_categoria:
            query = query.filter(categoria__icontains=filtro_categoria)

        if filtro_marca:
            query = query.filter(marca__nombre = filtro_marca)
        return query
    
class ComprarProducto(CreateView):
    model = Compra
    template_name = 'ap/compra_producto.html'
    formClass = CreaCompra
    success_url = 'lista'

class RegistraUsuario(CreateView):
    model = Usuario
    template_name = 'registration/registra.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('lista') #se pone el name de las url