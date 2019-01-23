from django.db import models
from django.shortcuts import reverse

class Empresa(models.Model):
    nom_empresa = models.CharField(max_length=100, help_text='Nome da Empresa')

    def __str__(self):
        return self.nom_empresa

    def get_absolute_url(self):
        return reverse('home')
