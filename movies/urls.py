from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_peliculas, name='listar_peliculas'),
    path('popularidad', views.listar_popularidad, name='lista_popularidad'),
    path('duracion', views.listar_duracion, name='lista_duracion'),
    path('fecha', views.listar_fecha, name='lista_fecha'),
]