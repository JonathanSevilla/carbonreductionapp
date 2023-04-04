from django.db import models

# Create your models here.
class TipoEmision(models.Model):
    nombre = models.CharField("nombre", max_length=150)

    def __str__(self):
        return self.nombre


class CategoriaConsumoCombustible(models.Model):
    nombre = models.CharField("nombre", max_length=150)

    def __str__(self):
        return self.nombre
    

class ConsumoCombustible(models.Model):
    id_categoria_consumo_combustible = models.ForeignKey(
        CategoriaConsumoCombustible,
        on_delete=models.CASCADE
    )
    fecha_registro = models.DateField()
    cantidad = models.FloatField()
    id_tipo_emision = models.ForeignKey(
        TipoEmision,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.id_categoria_consumo_combustible.nombre + " " + self.id_tipo_emision.nombre


