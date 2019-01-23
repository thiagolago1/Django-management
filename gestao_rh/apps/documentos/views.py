from .models import Documento
from django.views.generic import CreateView

class DocumentoCreate(CreateView):
    model = Documento
    fields = ['dsc_documento', 'arquivo']