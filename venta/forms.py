from .models import Plataforma, Categoria, Coleccion
from django.forms import ModelForm

class PlataformaForm(ModelForm):
    class Meta:
        model = Plataforma
        fields = ["plataforma"]
        labels = {"plataforma": "Plataforma",}


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ["categoria"]
        labels = {"categoria": "Categoria",}

class ColeccionForm(ModelForm):
    class Meta:
        model = Coleccion
        fields = ["coleccion"]
        labels = {"coleccion": "Coleccion",}