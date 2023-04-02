from django.urls import path
from . import views

urlpatterns = [
    path('post-registro-viajes/',  views.post_registro_viajes),
    path('comparativa-viajes/',  views.comparativa_viajes),

]