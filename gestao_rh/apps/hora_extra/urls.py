from django.urls import path
from .views import HoraExtraList

urlpatterns = [
    path('', HoraExtraList.as_view(), name="list_hora_extra"),
    # path('editar/<int:pk>/', funcionariosUpdate.as_view(), name="update_funcionario"),
    # path('delete/<int:pk>/', funcionariosDelete.as_view(), name="delete_funcionario"),
    # path('novo/', funcionariosNovo.as_view(), name="create_funcionario"),
]
