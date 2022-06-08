from django.urls import path
from chapDengue.views.ListarVisitasView import listar_visitas_view

urlpatterns = [
    path("", listar_visitas_view, name='listarVisitas'),
]