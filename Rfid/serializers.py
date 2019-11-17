from rest_framework import routers, serializers, viewsets

from Rfid.models import Rfid

class RfidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rfid
        fields = ('__all__')