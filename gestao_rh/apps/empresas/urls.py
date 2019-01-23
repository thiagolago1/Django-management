from django.urls import path
from .views import EmpresaForm
from .views import EmpresaEdit

urlpatterns = [
    path('novo', EmpresaForm.as_view(), name="empresa_form"),
    path('editar/<int:pk>/', EmpresaEdit.as_view(), name="empresa_edit"),

]
