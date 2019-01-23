from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView 
from .models import Empresa
from django.http import HttpResponse

class EmpresaForm(CreateView):
    model = Empresa
    fields = ['nom_empresa']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('Ok')

class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nom_empresa']