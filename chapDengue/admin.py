from email.mime import image
from django.contrib import admin
from .models import *

# Crie o método a seguir em seu arquivo
class ProfileAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'created_at'
    list_display = ('user', 'role', 'image')
    empty_value_display = 'Vazio'
    list_filter = ('user__is_active',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Agente)
admin.site.register(Visita)


