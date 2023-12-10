from django.db import models
from django.utils import timezone
from decimal import Decimal

class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad = models.IntegerField()
   

    def __str__(self):
        return self.nombre

class Habitacion(models.Model):
    numero = models.CharField(max_length=10)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)

    def __str__(self):
        return f'Habitación {self.numero} - {self.tipo}'

class Huesped(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class TipoPago(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# models.py

class Reserva(models.Model):
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    huesped = models.CharField(max_length=255, verbose_name='Nombre del huésped')
    fecha_llegada = models.DateField()
    fecha_salida = models.DateField()
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE, null=True, blank=True)
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2, default=0)  
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def save(self, *args, **kwargs):
        # Calcula el total_pagar antes de guardar la reserva
        if self.habitacion:
            self.total_pagar = Decimal(str(self.habitacion.costo))
            # Calcula el 20% del monto total
            self.monto_pagado = Decimal('0.2') * self.total_pagar
        super().save(*args, **kwargs)


    def __str__(self):
        return f'Reserva para {self.huesped} - Habitación {self.habitacion.numero}'

