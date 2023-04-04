import ast
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.decorators import api_view
from .models import (
    CategoriaConsumoEnergiaElectirca,
    ConsumoEnergiaElectirca
)
from applications.combustible.models import (
    ConsumoCombustible
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

# Comparativa de uso mensual entre energía eléctrica y uso de
# combustible (en porcentaje)
def procentaje(total_porcentaje,porcentaje):
    resultado = round(float((porcentaje / total_porcentaje) * 100),2)
    return resultado


@api_view(['GET'])
def energia_vs_combustible_porcentaje_mensual(request):
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
    dict_consumo_energia_combustible = {}
    dict_combustible = {}
    dict_energia = {}

    for i in range(1,13 ):
        mensual_energia = ConsumoEnergiaElectirca.objects.filter(fecha_registro__month=i) \
                .aggregate(Sum('cantidad'))
        mensual_combustible = ConsumoCombustible.objects.filter(fecha_registro__month=i) \
                .aggregate(Sum('cantidad'))
        
        resultado_energia = mensual_energia['cantidad__sum']
        resultado_combustible = mensual_combustible['cantidad__sum']
        valor_energia = 0
        valor_combustible = 0

        igual_none = "Consumo no registrado en esa fecha"

        if resultado_energia == None or resultado_combustible == None:               
            total_consumo = igual_none
            valor_energia = igual_none
            valor_combustible = igual_none

        else:
            total_consumo = resultado_combustible + resultado_energia
            valor_energia = procentaje(total_consumo,resultado_energia) 
            valor_combustible = procentaje(total_consumo,resultado_combustible)

        dict_combustible["Consumo Combustible " + meses[i]] = valor_combustible
        dict_energia["Consumo Energia " + meses[i]] = valor_energia

        key_combustible, value_combustible = list(dict_combustible.keys())[-1], list(dict_combustible.values())[-1]
        key_energia, value_energia = list(dict_energia.keys())[-1], list(dict_energia.values())[-1]

        if valor_combustible == igual_none:
            combustible = "{"+"'{}' : '{}'".format(key_combustible, value_combustible)+" ,"

        if  value_energia == igual_none:
            energia = " "+"'{}' : '{}'".format(key_energia, value_energia)+"}"
        
        if valor_combustible != igual_none and value_energia != igual_none:
            combustible = "{"+"'{}' : {}".format(key_combustible, value_combustible)+" ,"                      
            energia = " "+"'{}' : {}".format(key_energia, value_energia)+"}"
        
        
        dict_consumo_energia_combustible[meses[i]] = ast.literal_eval(combustible + energia)

    return Response(dict_consumo_energia_combustible)