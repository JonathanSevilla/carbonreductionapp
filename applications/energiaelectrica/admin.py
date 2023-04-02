from django.contrib import admin
from .models import (
    CategoriaConsumoEnergiaElectirca,
    ConsumoEnergiaElectirca
)

# Register your models here.
admin.site.register(CategoriaConsumoEnergiaElectirca)
admin.site.register(ConsumoEnergiaElectirca)
