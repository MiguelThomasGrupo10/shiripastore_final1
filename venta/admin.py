from django.contrib import admin
from .models import Inventario, Plataforma, Categoria, Coleccion

# Register your models here.
admin.site.register(Inventario)
admin.site.register(Plataforma)
admin.site.register(Categoria)
admin.site.register(Coleccion)
