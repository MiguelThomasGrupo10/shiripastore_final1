#   se importan random y string
import random
import string
from django.db import models
# Create your models here.
  
#Modelo de la tabla VENTA

class Categoria(models.Model):
    Id_categoria     = models.AutoField(db_column='idCategoria', primary_key=True)
    categoria        = models.CharField(unique = True, max_length=50)
    
    def __str__(self):
        return str(self.categoria) 

class Plataforma(models.Model):
    Id_plataforma    = models.AutoField(db_column='idPlataforma',primary_key=True)
    plataforma       = models.CharField(unique = True, max_length=50)

    def __str__(self):
        return str(self.plataforma) 


class Inventario(models.Model):
    DISPONIBILIDAD_CHOICES = (
        ('disponible', 'Disponible'),
        ('no_disponible', 'No disponible'),
    )
    
    Id_juego         = models.AutoField(primary_key=True)
    Id_categoria     = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='idCategoria')
    Id_plataforma    = models.ForeignKey('Plataforma', on_delete=models.CASCADE, db_column='idPlataforma')
    nombre_juego     = models.CharField(max_length=30) 
    valor            = models.DecimalField(max_digits=8, decimal_places=2)  
    stock            = models.IntegerField(default=100)  
    disponible       = models.CharField(max_length=20, choices=DISPONIBILIDAD_CHOICES)

    def __str__(self):
        return str(self.nombre_juego)+" "+str(self.plataforma)

#Tablas de Boleta, Categoria, Plataforma




# class Boleta(models.Models):
#     Id_boleta     = models.BigAutoField(primary_key=True)
#     Id_usuario    = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
#     Id_inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
#     nombre_juego  = models.CharField(max_length=30)
#     valor         = models.DecimalField(max_digits=8, decimal_places=2)
#     licencia      = models.CharField(max_length=10, default=generar_codigo_licencia) #aquí se utiliza la función
#     email         = models.EmailField()

#     def __str__(self):
#         return str(self.Id_boleta)

    
    

