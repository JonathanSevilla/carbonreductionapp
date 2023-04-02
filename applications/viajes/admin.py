from django.contrib import admin
from .models import (
    EquiposViaje,
    Viajes    
)

# Register your models here.
admin.site.register(EquiposViaje)
admin.site.register(Viajes)
