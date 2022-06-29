from django.http import HttpResponse
from chapDengue.models import Agente
from django.shortcuts import render, redirect
from chapDengue.models import Profile
from django.db.models import Q


def list_agente_view(request):
   agentes = Agente.objects.all()
   
   ##if name is not None and name !='':
     ##  agentes = agentes.filter(user__frist_name=name)
   
   context = {
         'agentes':agentes,
     }

   return render(request, template_name='agentes/agentes.html', context=context, status=200)

