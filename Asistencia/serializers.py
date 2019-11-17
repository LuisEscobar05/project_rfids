from rest_framework import routers, serializers, viewsets

from Asistencia.models import Asistencia

class AsistenciaSerializer(serializers.ModelSerializer):
    nombre_alumno = serializers.ReadOnlyField(source = "id_alumno.name")
    class Meta:
        model = Asistencia
        fields = ('__all__')