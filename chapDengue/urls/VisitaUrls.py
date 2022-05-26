from django.urls import path
from chapDengue.views.VisitaView import list_visitas_view

urlpatterns = [
    path("", list_visitas_view, name='visitas'),
]