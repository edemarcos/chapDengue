from django.urls import path
from chapDengue.views.AgenteView import list_agentes_view

urlpatterns = [
    path("", list_agentes_view, name='agentes'),
]

