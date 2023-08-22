from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ingresar/', views.ingresar_entrada, name='ingresar_entrada'),
    path('buscar/', views.buscar_entrada, name='buscar_entrada'),
]