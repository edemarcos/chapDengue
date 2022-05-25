from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Agente'),
    (3, 'Usuário')
)

from .Visita import Visita
from .Agente import Agente
from .Cidade import Cidade
from .Estado import Estado
from .Profile import Profile

