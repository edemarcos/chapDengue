from chapDengue.models import *

class Cidade(models.Model):
    estado = models.ForeignKey("Estado", null=True, on_delete=models.SET_NULL, related_name='estado')
    name = models.CharField(null=False, max_length=20)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}-{}'.format(self.name, self.estado.sigla)

