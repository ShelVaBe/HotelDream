from django.urls import path
from . import views

urlpatterns = [
    #path('Reservar/', views.reservar_view, name='Reservar'),
    path('reservacion/', views.reservacion, name='reservacion'),   
]