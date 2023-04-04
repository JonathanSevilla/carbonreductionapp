from rest_framework import serializers
from .models import (
    CategoriaConsumoDerivadosPetroleo,
    ConsumoDerivadosPetroleo,
    TipoAceite,
    TipoRefrigerante,
    Aceite,
    Refrigerante
)

class CategoriaConsumoDerivadosPetroleoSerializers(serializers.ModelSerializer):

    class Meta:
        model = CategoriaConsumoDerivadosPetroleo
        fields = '__all__'


class ConsumoDerivadosPetroleoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = ConsumoDerivadosPetroleo
        fields = '__all__'


class TipoAceiteSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = TipoAceite
        fields = '__all__'


class AceitesSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Aceite
        fields = '__all__'


class TipoRefrigeranteSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = TipoRefrigerante
        fields = '__all__'


class RefrigeranteSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Refrigerante
        fields = '__all__'