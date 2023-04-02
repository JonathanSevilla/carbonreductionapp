from rest_framework import serializers
from .models import (
    EquiposViaje,
    Viajes
)

class EquiposViajeSerializers(serializers.ModelSerializer):

    class Meta:
        model = EquiposViaje
        fields = '__all__'


class ViajesSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Viajes
        fields = '__all__'