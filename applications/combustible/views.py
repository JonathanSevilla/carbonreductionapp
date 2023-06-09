from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
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

class CombustibleViewset(viewsets.ViewSet):
    serializer_class = ConsumoCombustibleSerializers
    queryset = ConsumoCombustible.objects.all() 

@api_view(['PUT', 'DELETE'])
def combustible(request, pk):
    try:
        combustible = ConsumoCombustible.objects.get(pk=pk)
    except ConsumoCombustible.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ConsumoCombustibleSerializers(combustible, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({})

    # elif request.method == 'DELETE':
    #     combustible.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


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


@api_view(['GET'])
def mayor_menor_uso_combustible(request): 
    meses = {
        1:"Enero",
        2:"Febrero",
        3:"Marzo",
        4:"Abril",
        5:"Mayo",
        6:"Junio",
        7:"Julio",
        8:"Agosto",
        9:"Septiembre",
        10:"Octubre",
        11:"Noviembre",
        12:"Diciembre"
    }
    
    combustible = {}
    combustible_max_min = {}
    list_combustible = []

    for i in range(1,13 ):  
        mensual_combustible = ConsumoCombustible.objects.filter(fecha_registro__month=i) \
            .aggregate(Sum('cantidad'))
            
        resultado_combustible = mensual_combustible['cantidad__sum']

        igual_none = 0          

        if resultado_combustible == None:               
            total_consumo = igual_none            
        
        else:
            total_consumo = resultado_combustible
            list_combustible.append(mensual_combustible['cantidad__sum'])
        
        combustible[meses[i]] = total_consumo

    value_min = min(list_combustible)
    value_max = max(list_combustible)
    
    key_min = list(combustible.keys())[list(combustible.values()).index(value_min)]
    key_max = list(combustible.keys())[list(combustible.values()).index(value_max)]
    combustible_max_min["Menor perdida de combustible en el mes de "+key_min] = value_min
    combustible_max_min["Meyor perdida de combustible en el mes de "+key_max] = value_max
    
    return Response(combustible_max_min)