from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import (
    CategoriaConsumoDerivadosPetroleo,
    ConsumoDerivadosPetroleo
)
from .serializers import (
    CategoriaConsumoDerivadosPetroleoSerializers,
    ConsumoDerivadosPetroleoSerializers,
)

# Create your views here.
@api_view(['POST'])
def post_consumo_derivados_petroleo(request):
    if request.method == 'POST':
        serializer = ConsumoDerivadosPetroleoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def uso_mensual_derivados_petroleo(request):
    i = 0
    dict_derivados = {
        'combustible':2500,
        'gases refrigerantes':3,
        'aceite':930
    }
    derivados = {}

    total_derivados = sum(dict_derivados.values())
    numero_derivados = list(dict_derivados)

    for n in numero_derivados:
        derivados[n] = round(float(float(list(dict_derivados.values())[i] / total_derivados) * 100 ),2)
        i += 1
    
    return Response(derivados)
