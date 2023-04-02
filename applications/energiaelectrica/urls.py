from django.urls import path
from . import views

urlpatterns = [
    # path('', include(router.urls)),
    path('post-derivados-petroleo/', views.post_consumo_energia_electrica),
    path('promedio-mensual-planta-envasado/', views.promedio_mensual_planta_envasado),
]