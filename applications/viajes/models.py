from django.db import models
from applications.combustible.models import TipoEmision


class EquiposViaje(models.Model):
    nombre = models.CharField("nombre", max_length=150)

    def __str__(self):
        return self.nombre
    

class Viajes(models.Model):
    fecha_registro = models.DateField(auto_now_add=True)
    id_equipos_viaje = models.ForeignKey(EquiposViaje, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    id_tipo_emision = models.ForeignKey(TipoEmision, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_equipos_viaje.nombre + " " + self.id_tipo_emision.nombre
