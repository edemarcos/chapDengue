from chapDengue.models import *

class Estado(models.Model):
    name = models.CharField(null=False, max_length=20)
    sigla = models.CharField(null=False, max_length=2)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}-{}'.format(self.name, self.sigla)

