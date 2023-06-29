from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name = 'index'),
    path('index/', views.index,name = 'index'),
    path('nosotros/', views.nosotros),
    path('carrito/',views.carrito),
    path('micuenta/',views.micuenta),
    path('tienda/',views.tienda),
    path('contacto/',views.contacto),
    path('formRegistro/',views.formRegistro),
]