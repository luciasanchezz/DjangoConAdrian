from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = Usuario
    # Agregar los nuevos campos a fieldsets (para edición de usuario)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('vip','saldo')}),  # Agrega solo los nuevos campos
    )

    # Agregar los nuevos campos a add_fieldsets (para crear usuario)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('vip','saldo')}),
    )

admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Compra)
