from rest_framework import serializers
from apps.hora_extra.models import RegistroHoraExtra


class RegistroHoraExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroHoraExtra
        fields = ('dsc_motivo', 'funcionario', 'horas', 'utilizada')