from django.http import HttpResponse
from chapDengue.models import Agente


def list_agentes_view(request):
   name = request.GET.get("name")
   status = request.GET.get("status")
   agentes = Agente.objects.all()
   
   ##if name is not None and name !='':
     ##  agentes = agentes.filter(user__frist_name=name)
   
   print(agentes)

   return HttpResponse('Listagem de 1 ou mais agentes')

