from django.urls import path
from . import views

urlpatterns = [
    #path('Reservar/', views.reservar_view, name='Reservar'),
    path('reservacion/', views.reservacion, name='reservacion'),   
    path('reservacion_exitosa/<int:reserva_id>/', views.reservacion_exitosa, name='reservacion_exitosa'),

]