from ast import arguments
from django.shortcuts import render, redirect
from chapDengue.models import Visita
from chapDengue.models import Profile
from django.db.models import Q
from django.core.paginator import Paginator

def listar_visitas_view(request):
     cidade = request.GET.get("Cidade")
     agente = request.GET.get("agente")
     rua = request.GET.get("rua")
     complemento = request.GET.get("complemento")
     descricao = request.GET.get("descricao")
     focos = request.GET.get("focos")
     dia = request.GET.get("dia")
   
     visitas = Visita.objects.all()

     if cidade is not None:
        visitas = Visita.filter(cidade__name=cidade)
        
     if agente is not None:
        visitas = Visita.filter(agente__name=agente)
        
     if rua is not None:
        visitas = Visita.filter(visita__rua=rua)
        
     if complemento is not None:
        visitas = Visita.filter(visita__complemento=complemento)

     if descricao is not None:
        visitas = Visita.filter(visita__descricao=descricao)
        
     if focos is not None:
        visitas = Visita.filter(visita__focos=focos)
   
     if dia is not None:
        visitas = Visita.filter(visita__dia=dia)
        
     if len(visitas) > 0:
         paginator = Paginator(visitas, 8)
         page = request.GET.get('page')
         visitas = paginator.get_page(page)

     get_copy = request.GET.copy()
     parameters = get_copy.pop('page', True) and get_copy.urlencode()

        
     context = {
         'visitas':visitas,
         'parameters': parameters
     }

     return render(request, template_name='visitas/visitas.html', context=context, status=200)

def add_favorite_view(request):
      page = request.POST.get("page")
      cidade = request.POST.get("Cidade")
      agente = request.POST.get("agente")
      rua = request.POST.get("rua")
      complemento = request.POST.get("complemento")
      descricao = request.POST.get("descricao")
      focos = request.POST.get("focos")
      dia = request.POST.get("dia")
      id = request.POST.get("id")
      
      try:
            profile = Profile.objects.filter(user=request.user).first()
            medic = Profile.objects.filter(user__id=id).first()
            profile.favorites.add(medic.user)
            profile.save()
            msg = "Favorito adicionado com sucesso"
            _type = "success"
      except Exception as e:
         print("Erro %s" % e)
         msg = "Um erro ocorreu ao salvar o médico nos favoritos"
         _type = "danger"

      if page:
            arguments = "?page=%s" % (page)
      else:
            arguments = "?page=1"
      
      arguments += "&msg=%s&type=%s" % (msg, _type)
      return redirect(to='/medic/%s' % arguments)


   

