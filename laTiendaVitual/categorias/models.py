from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    nombre = models.CharField(max_length=100 , null=False, unique=True, verbose_name='Nombre categoría')