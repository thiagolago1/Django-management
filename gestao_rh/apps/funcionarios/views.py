from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class funcionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class funcionariosUpdate(UpdateView):
    model = Funcionario
    fields = ['nom_funcionario', 'departamentos']

class funcionariosDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionario_list')

class funcionariosNovo(CreateView):
    model = Funcionario
    fields = ['nom_funcionario', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nom_funcionario
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(funcionariosNovo, self).form_valid(form)