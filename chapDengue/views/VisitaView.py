from chapDengue.models import Visita
from django.shortcuts import render, redirect
from django.contrib import messages
from chapDengue.forms.CadVisitaForm import CadVisita

def cad_visita_view(request):
   data = {}
   data['cadVisitaForm'] = CadVisita()
   return render(request, 'visita/cadvisita.html', data)
   