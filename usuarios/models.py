from django.db import models

# Create your models here.

# modelo de la tabla USUARIO
class Usuarios(models.Model):
    id_usuario       = models.BigAutoField(primary_key=True)
    nombre           = models.CharField(max_length=40)
    apellidos        = models.CharField(max_length=50)
    email            = models.EmailField(unique=True, max_length=100)
    contrasenna      = models.CharField(max_length=20)  
    activo           = models.IntegerField(default=1)

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellidos) 