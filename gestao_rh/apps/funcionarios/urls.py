from django.urls import path
from .views import ( 
    funcionariosList, funcionariosUpdate, funcionariosDelete, funcionariosNovo, Pdf #PdfDebug 
    )
from .views import relatorio_funcionarios

urlpatterns = [
    path('', funcionariosList.as_view(), name="funcionario_list"),
    path('editar/<int:pk>/', funcionariosUpdate.as_view(), name="update_funcionario"),
    path('delete/<int:pk>/', funcionariosDelete.as_view(), name="delete_funcionario"),
    path('novo/', funcionariosNovo.as_view(), name="create_funcionario"),
    path('relatorio_funcionarios', relatorio_funcionarios, name='relatorio_funcionarios'),
    path('relatorio_funcionarios_html', Pdf.as_view(), name='relatorio_funcionarios_html'),
    #path('relatorio_funcionarios_html_debug', PdfDebug.as_view(), name='relatorio_funcionarios_html_debug'),
]
