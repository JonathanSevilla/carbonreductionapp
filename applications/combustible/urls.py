from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('post-consumo-combustible/', views.post_consumo_combustible),
    path('porcentaje-consumo-anual-combustible/',  views.porcentaje_consumo_anual_combustible),
    path('porcentaje-consumo-mensual-combustible/',  views.porcentaje_consumo_mensual_combustible),
    path('segmento-mayor-impacta/', views.segmento_mayor_impacta)

]