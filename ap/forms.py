from .models import *
from django import forms 
from django.contrib.auth.forms import UserCreationForm

class CreaProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class CreaCompra(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'email']