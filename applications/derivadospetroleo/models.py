from django.db import models
from applications.combustible.models import TipoEmision


class CategoriaConsumoDerivadosPetroleo(models.Model):
    nombre = models.CharField("nombre", max_length=150)

    def __str__(self):
        return self.nombre
    

class ConsumoDerivadosPetroleo(models.Model):
    id_categoria_consumo_derivados = models.ForeignKey(
        CategoriaConsumoDerivadosPetroleo,
        on_delete=models.CASCADE
    )
    fecha_registro = models.DateField(auto_now_add=True)
    cantidad = models.FloatField()
    id_tipo_emision = models.ForeignKey(TipoEmision, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_categoria_consumo_derivados.nombre + " " + self.id_tipo_emision.nombre