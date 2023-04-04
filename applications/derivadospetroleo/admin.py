from django.contrib import admin
from .models import (
    CategoriaConsumoDerivadosPetroleo,
    ConsumoDerivadosPetroleo,
    TipoAceite,
    TipoRefrigerante,
    Aceite,
    Refrigerante
)

# Register your models here.
admin.site.register(CategoriaConsumoDerivadosPetroleo)
admin.site.register(ConsumoDerivadosPetroleo)
admin.site.register(TipoAceite)
admin.site.register(Aceite)
admin.site.register(TipoRefrigerante)
admin.site.register(Refrigerante)