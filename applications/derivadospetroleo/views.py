import ast
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.decorators import api_view
from .models import (
    CategoriaConsumoDerivadosPetroleo,
    ConsumoDerivadosPetroleo,
    Aceite,
    Refrigerante
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

# Mostrar los datos de uso de aceites mensualmente
#  (En galones)
@api_view(['GET'])
def aceites_mensual(request): 
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
    aceites = {}
    dict_aceite = {}

    for i in range(1,13 ):  
        mensual_aceite = Aceite.objects.filter(fecha_registro__month=i) \
            .aggregate(Sum('cantidad_galones'))
            
        resultado_aceite = mensual_aceite['cantidad_galones__sum']
        valor_aceite = 0

        igual_none = "Consumo no registrado en esta fecha"

        if resultado_aceite == None:               
            total_consumo = igual_none
            valor_aceite = igual_none
        
        else:
            total_consumo = resultado_aceite

        dict_aceite["Consumo en galones de aceite " + meses[i]] = total_consumo

        key, value = list(dict_aceite.keys())[-1], list(dict_aceite.values())[-1]

        if valor_aceite == igual_none:
            aceite = "{"+"'{}' : '{}'".format(key, value)+" }"

        
        if valor_aceite != igual_none:
            aceite = "{"+"'{}' : {}".format(key, value)+" }"

        aceites[meses[i]] = ast.literal_eval(aceite)
    print(aceites)                    
    
    return Response(aceites)


@api_view(['GET'])
def menos_perdidas_refrigerante(request): 
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

    refrigerante = {}
    refrigerante_min = {}
    list_refrigerante = []

    for i in range(1,13 ):  
        mensual_refrigerante = Refrigerante.objects.filter(fecha_registro__month=i) \
            .aggregate(Sum('cantidad_galones'))
            
        resultado_refrigerante = mensual_refrigerante['cantidad_galones__sum']

        igual_none = 0          

        if resultado_refrigerante == None:               
            total_consumo = igual_none            
        
        else:
            total_consumo = resultado_refrigerante
            list_refrigerante.append(mensual_refrigerante['cantidad_galones__sum'])
        
        refrigerante[meses[i]] = total_consumo

    value_min = min(list_refrigerante)
    
    key_min = list(refrigerante.keys())[list(refrigerante.values()).index(value_min)]  
    refrigerante_min["Menor perdida de Refrigerante en el mes de "+key_min] = value_min 
    print(refrigerante_min)

    return Response(refrigerante_min)