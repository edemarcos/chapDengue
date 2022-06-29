from django.urls import path
from chapDengue.views.AgenteView import list_agente_view

urlpatterns = [
    path("", list_agente_view, name='agentes'),
]

