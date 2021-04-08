from django.urls import path

from . import views


urlpatterns = [
    path('buscar_personaje/', views.buscar_personaje, name='buscar'),
    path('', views.index, name='index'),
    path('<str:serie>/', views.temporadas, name='temporadas'),
    path('<str:serie>/<int:n_temporada>/', views.episodios, name='episodios'),
    path('<str:serie>/<int:n_temporada>/<int:n_episodio>/', views.detalle_episodios, name='detalle_episodios'),
    path('personajes/<str:nombre_personaje>/', views.personaje, name='personajes'),
]