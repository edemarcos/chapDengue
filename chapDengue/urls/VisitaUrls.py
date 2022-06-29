from django.urls import path
from chapDengue.views.VisitaView import cad_visita_view

urlpatterns = [
    path("registrarVisita/", cad_visita_view, name='cadvisita'),
]