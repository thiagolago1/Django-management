from django.db import models
from apps.funcionarios.models import Funcionario
from django.urls import reverse

class RegistroHoraExtra(models.Model):
    dsc_motivo = models.CharField(max_length=200)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)
    utilizada = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.id])

    def __str__(self):
        return self.dsc_motivo