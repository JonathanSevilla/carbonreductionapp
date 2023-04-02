from django.db import models
from applications.combustible.models import TipoEmision


class CategoriaConsumoEnergiaElectirca(models.Model):
    nombre = models.CharField("nombre", max_length=150)

    def __str__(self):
        return self.nombre
    

class ConsumoEnergiaElectirca(models.Model):
    id_categoria_consumo_enerigia = models.ForeignKey(
        CategoriaConsumoEnergiaElectirca,
        on_delete=models.CASCADE
    )
    cantidad = models.FloatField()
    fecha_registro = models.DateField(auto_now_add=True)
    id_tipo_emision = models.ForeignKey(
        TipoEmision,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.id_categoria_consumo_enerigia.nombre + " " + self.id_tipo_emision.nombre
