from django.shortcuts import render
from chapDengue.models import Visita
from django.db.models import Q

def listar_visitas_view(request):
     cidade = request.GET.get("cidade")
     agente = request.GET.get("agente")
     rua = request.GET.get("rua")
     complemento = request.GET.get("complemento")
     descricao = request.GET.get("descricao")
     focos = request.GET.get("focos")
     dia = request.GET.get("dia")
     status = request.GET.get("status")
     visita = Visita.objects.all()

     if cidade is not None:
        visita = Visita.filter(cidade__name=cidade)
        
     if agente is not None:
        visita = Visita.filter(agente__name=agente)
        
     if rua is not None:
        visita = Visita.filter(visita__rua=rua)
        
     if complemento is not None:
        visita = Visita.filter(visita__complemento=complemento)

     if descricao is not None:
        visita = Visita.filter(visita__descricao=descricao)
        
     if focos is not None:
        visita = Visita.filter(visita__focos=focos)
   
     if dia is not None:
        visita = Visita.filter(visita__dia=dia)
        
        context = {
            'visitas':visita
        }

     return render(request, template_name='visitas/visitas.html', context=context, status=200)

