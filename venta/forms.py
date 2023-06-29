from .models import Plataforma, Categoria
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