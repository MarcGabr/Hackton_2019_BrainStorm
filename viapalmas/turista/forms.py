from django.forms import ModelForm
from .models import Turista

class TuristaForm(ModelForm):
    class Meta:
        model = Turista
        fields = ['nome', 'telefone']