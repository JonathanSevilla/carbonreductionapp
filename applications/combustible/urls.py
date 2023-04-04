from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('post-consumo-combustible/', views.post_consumo_combustible),
    path('put-combustibles/<int:pk>/', views.combustible),
    path('porcentaje-consumo-anual-combustible/',  views.porcentaje_consumo_anual_combustible),
    path('porcentaje-consumo-mensual-combustible/',  views.porcentaje_consumo_mensual_combustible),
    path('segmento-mayor-impacta/', views.segmento_mayor_impacta),
    path('mayor-menor-uso-combustible/', views.mayor_menor_uso_combustible),
]