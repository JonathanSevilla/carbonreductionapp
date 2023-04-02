from django.contrib import admin
from .models import (
    CategoriaConsumoDerivadosPetroleo,
    ConsumoDerivadosPetroleo
)

# Register your models here.
admin.site.register(CategoriaConsumoDerivadosPetroleo)
admin.site.register(ConsumoDerivadosPetroleo)