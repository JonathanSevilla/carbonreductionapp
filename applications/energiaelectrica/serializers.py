from rest_framework import serializers
from .models import (
    CategoriaConsumoEnergiaElectirca,
    ConsumoEnergiaElectirca
)

class CategoriaConsumoEnergiaElectircaSerializers(serializers.ModelSerializer):

    class Meta:
        model = CategoriaConsumoEnergiaElectirca
        fields = '__all__'


class ConsumoEnergiaElectircaSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = ConsumoEnergiaElectirca
        fields = '__all__'