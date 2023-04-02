from rest_framework import serializers
from .models import (
    CategoriaConsumoDerivadosPetroleo,
    ConsumoDerivadosPetroleo
)

class CategoriaConsumoDerivadosPetroleoSerializers(serializers.ModelSerializer):

    class Meta:
        model = CategoriaConsumoDerivadosPetroleo
        fields = '__all__'


class ConsumoDerivadosPetroleoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = ConsumoDerivadosPetroleo
        fields = '__all__'