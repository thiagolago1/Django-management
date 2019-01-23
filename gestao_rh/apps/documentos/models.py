from django.db import models
from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    dsc_documento = models.CharField(max_length=100)
    dsc_pertence_funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def __str__(self):
        return self.dsc_documento