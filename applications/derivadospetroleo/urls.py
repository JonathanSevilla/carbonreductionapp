from django.urls import path
from . import views

urlpatterns = [
    path('post-derivados-petroleo/', views.post_consumo_derivados_petroleo),
    path('uso-mensual-productos-derivados-petróleo/', views.uso_mensual_derivados_petroleo),
    path('aceites-mensual/', views.aceites_mensual),
    path('menos-perdidas-refrigerante/', views.menos_perdidas_refrigerante)
]