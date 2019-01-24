from .models import Documento
from django.views.generic import CreateView

class DocumentoCreate(CreateView):
    model = Documento
    fields = ['dsc_documento', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.dsc_pertence_funcionario_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)