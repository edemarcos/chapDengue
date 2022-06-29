from dataclasses import fields
from django.forms import ModelForm
from chapDengue.models import Visita

class CadVisita(ModelForm):
    class Meta:
        model: Visita
        fields = ['cidade','agente', 'rua', 'complemento', 'descricao', 'focos', 'dia']