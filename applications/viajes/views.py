from rest_framework import status
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.decorators import api_view
import ast

from .models import (
    EquiposViaje,
    Viajes
)
from .serializers import (
    EquiposViajeSerializers,
    ViajesSerializers,
)

# Create your views here.
@api_view(['POST'])
def post_registro_viajes(request):
    if request.method == 'POST':
        serializer = ViajesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def Merge(dict1, dict2):
    return(dict2.update(dict1))

# Comparativa de promedio mensual de viajes equipo de ventas y
# equipo administrativo
# (En cantidad de viajes)
@api_view(['GET'])
def comparativa_viajes(request):
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
    viajes = {}
    dict_venta = {}
    dict_admin = {}

    for i in range(1,13 ):
        viajes_ventas = Viajes.objects.filter(fecha_registro__month=i, id_equipos_viaje=1) \
            .aggregate(Sum('cantidad'))
        viajes_administracion = Viajes.objects.filter(fecha_registro__month=i, id_equipos_viaje=2) \
            .aggregate(Sum('cantidad'))

        valor_mes_ventas = viajes_ventas['cantidad__sum']
        valor_mes_admin = viajes_administracion['cantidad__sum']

        dict_venta["Viajes de Ventas "+meses[i]] = valor_mes_ventas
        dict_admin["Viajes de Administracion "+meses[i]] = valor_mes_admin

        key_admin, value_admin = list(dict_admin.keys())[-1], list(dict_admin.values())[-1]
        admin = "{"+"'{}' : {}".format(key_admin, value_admin)+" ,"

        key_venta, value_venta = list(dict_venta.keys())[-1], list(dict_venta.values())[-1]
        ventas = " "+"'{}' : {}".format(key_venta, value_venta)+"}"

        viajes[meses[i]] = ast.literal_eval(admin + ventas)
    
    return Response(viajes)


