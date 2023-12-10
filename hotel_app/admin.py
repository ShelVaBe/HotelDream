from django.contrib import admin
from .models import TipoHabitacion, TipoPago, Huesped, Habitacion, Reserva

# Registra tus modelos aquí
admin.site.register(TipoHabitacion)
admin.site.register(TipoPago)
admin.site.register(Huesped)
admin.site.register(Habitacion)
admin.site.register(Reserva)