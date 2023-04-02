from rest_framework import status
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.decorators import api_view
from .models import (
    TipoEmision,
    CategoriaConsumoCombustible,
    ConsumoCombustible
)
from .serializers import (
    TipoEmisionSerializers,
    CategoriaConsumoCombustibleSerializers,
    ConsumoCombustibleSerializers
)


# Create your views here.
@api_view(['POST'])
def post_consumo_combustible(request):
    if request.method == 'POST':
        serializer = ConsumoCombustibleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# function-based view
@api_view(['GET'])
def calculate(request, a, b):
    result = a + b 
    return Response({"message": f"{result}"})

@api_view(['GET'])
def porcentaje_consumo_anual_combustible(request):
    consumo_anual = {} 
    consumo_categoria = {}
    i = 0
    categorias = CategoriaConsumoCombustible.objects.all().values('id','nombre')
    list_categorias = list(categorias)

    for categoria in list_categorias:
        consumo = ConsumoCombustible.objects \
            .filter(id_categoria_consumo_combustible__id=categoria['id'], \
            fecha_registro__range=["2023-01-01", "2023-12-31"]) \
            .aggregate(Sum('cantidad'))
        
        porcentaje = consumo['cantidad__sum']
        consumo_anual[categoria['nombre']] = porcentaje

    total_consumo = sum(consumo_anual.values())    
    numero_categorias = list(consumo_anual)

    for categoria in numero_categorias:
        consumo_categoria[categoria] = round(float(list(consumo_anual.values())[i] / total_consumo) * 100,2)
        i += 1

    return Response(consumo_categoria)


@api_view(['GET'])
def porcentaje_consumo_mensual_combustible(request):
    consumo_mensual = {} 
    consumo_categoria = {}
    i = 0
    categorias = CategoriaConsumoCombustible.objects.all().values('id','nombre')
    list_categorias = list(categorias)

    for categoria in list_categorias:
        consumo = ConsumoCombustible.objects \
            .filter(id_categoria_consumo_combustible__id=categoria['id'], \
            fecha_registro__range=["2023-01-01", "2023-12-31"]) \
            .aggregate(Sum('cantidad'))
        
        porcentaje = consumo['cantidad__sum']
        consumo_mensual[categoria['nombre']] = porcentaje

    total_consumo = sum(consumo_mensual.values())    
    numero_categorias = list(consumo_mensual)

    for categoria in numero_categorias:
        consumo_categoria[categoria] = round(float(float(list(consumo_mensual.values())[i] / total_consumo) * 100 / 12),2)
        i += 1

    return Response(consumo_categoria)


@api_view(['GET'])
def segmento_mayor_impacta(request):
    consumo_mensual = {} 
    consumo_categoria = {}
    i = 0
    categorias = CategoriaConsumoCombustible.objects.all().values('id','nombre')
    list_categorias = list(categorias)

    for categoria in list_categorias:
        consumo = ConsumoCombustible.objects.filter(id_categoria_consumo_combustible__id=categoria['id'], fecha_registro__range=["2023-01-01", "2023-12-31"]).aggregate(Sum('cantidad'))
        porcentaje = consumo['cantidad__sum']
        consumo_mensual[categoria['nombre']] = porcentaje

    total_consumo = sum(consumo_mensual.values())    
    numero_categorias = list(consumo_mensual)

    for categoria in numero_categorias:
        consumo_categoria[categoria] = round(float(float(list(consumo_mensual.values())[i] / total_consumo) * 100 / 12),2)
        i += 1

    max_segmento = max(consumo_categoria, key=consumo_categoria.get)
    print(max_segmento)

    valor = max(consumo_categoria.values())

    return Response({max_segmento: valor})