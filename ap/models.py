from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    vip = models.BooleanField(default=False)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.first_name

class Marca(models.Model):
    nombre = models.CharField(max_length = 10)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.CharField(max_length = 15)
    marca = models.ForeignKey(Marca, max_length=10, on_delete = models.CASCADE, )
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    vip = models.BooleanField(default=False)
    def __str__(self):
        return self.categoria

class Compra (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    unidades = models.PositiveIntegerField()
    fecha = models.DateField(auto_now_add=True)
    importe = models.IntegerField()
    iva = models.DecimalField(decimal_places=2, max_digits=2, default=0.21)
    def __str__(self):
        return f'{self.usuario}'