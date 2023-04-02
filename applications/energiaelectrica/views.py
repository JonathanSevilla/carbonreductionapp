from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import (
    CategoriaConsumoEnergiaElectirca,
    ConsumoEnergiaElectirca
)
from .serializers import (
    CategoriaConsumoEnergiaElectircaSerializers,
    ConsumoEnergiaElectircaSerializers
)

# Create your views here.
@api_view(['POST'])
def post_consumo_energia_electrica(request):
    if request.method == 'POST':
        serializer = ConsumoEnergiaElectircaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def promedio_mensual_planta_envasado(request):
    planta_envasado = 900
    
    promedio = "Promedio mensual planta de envasado: "
    valor = planta_envasado / 3

    return Response({promedio: valor})

