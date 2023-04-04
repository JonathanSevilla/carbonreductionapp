from rest_framework import serializers
from .models import (
    TipoEmision,
    ConsumoCombustible,
    CategoriaConsumoCombustible
)

class TipoEmisionSerializers(serializers.ModelSerializer):

    class Meta:
        model = TipoEmision
        fields = '__all__'


class CategoriaConsumoCombustibleSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = CategoriaConsumoCombustible
        fields = '__all__'


class ConsumoCombustibleSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = ConsumoCombustible
        fields = '__all__'