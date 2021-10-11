from django.db import models
from categorias.models import Categoria

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name='Categoria')
    nombre = models.TextField(max_length=500, null=False, verbose_name='Nombre del producto')
    estado = models.SmallIntegerField(default=0, null=False, verbose_name='Estado')
    cantidad = models.IntegerField(default=0, null=False, verbose_name='Cantidad')

    def __str__(self) -> str:
        return self.nombre