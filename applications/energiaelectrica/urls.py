from django.urls import path
from . import views

urlpatterns = [
    path('post-consumo-energia-electrica/', views.post_consumo_energia_electrica),
    path('promedio-mensual-planta-envasado/', views.promedio_mensual_planta_envasado),
    path('energia-vs-combustible-porcentaje-mensual/', views.energia_vs_combustible_porcentaje_mensual)
]