from django.contrib import admin
from .models import (
    TipoEmision,
    CategoriaConsumoCombustible,
    ConsumoCombustible
)

# Register your models here.

admin.site.register(TipoEmision)
admin.site.register(CategoriaConsumoCombustible)
admin.site.register(ConsumoCombustible)
