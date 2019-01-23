from django.urls import path
from .views import funcionariosList, funcionariosUpdate, funcionariosDelete, funcionariosNovo

urlpatterns = [
    path('', funcionariosList.as_view(), name="funcionario_list"),
    path('editar/<int:pk>/', funcionariosUpdate.as_view(), name="update_funcionario"),
    path('delete/<int:pk>/', funcionariosDelete.as_view(), name="delete_funcionario"),
    path('novo/', funcionariosNovo.as_view(), name="create_funcionario"),
]
