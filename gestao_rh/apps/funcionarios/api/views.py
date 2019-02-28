from rest_framework import viewsets, serializers
from apps.funcionarios.api.serializers import FuncionarioSerializer
from apps.funcionarios.models import Funcionario
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'put', 'options']