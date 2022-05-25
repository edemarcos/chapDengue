from chapDengue.models import *

class Visita(models.Model):
    cidade = models.ForeignKey("Cidade", null=True, on_delete=models.SET_NULL, related_name='cidade')
    agente = models.ForeignKey("Agente", null=True, on_delete=models.SET_NULL, related_name='agente')
    rua = models.CharField(null=False, max_length=200)
    complemento = models.CharField(null=False, max_length=20)
    descricao = models.CharField(null=False, max_length=300)
    focos = models.IntegerField(null=False)
    dia = models.DateTimeField(null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

 