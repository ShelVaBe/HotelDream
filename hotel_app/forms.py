# forms.py

from django import forms
from .models import Reserva, Habitacion, TipoHabitacion

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['huesped', 'fecha_llegada', 'fecha_salida', 'tipo_pago', 'tipo_habitacion']

        widgets = {
          'huesped': forms.TextInput(attrs={'placeholder': 'Nombre del huésped'}),
          'fecha_llegada': forms.DateInput(attrs={'type': 'date'}),
          'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
    }
    def clean(self):
        cleaned_data = super().clean()
        fecha_llegada = cleaned_data.get('fecha_llegada')
        fecha_salida = cleaned_data.get('fecha_salida')
        tipo_habitacion = cleaned_data.get('tipo_habitacion')

        if fecha_llegada and fecha_salida and tipo_habitacion:
            # Verificar si hay habitaciones disponibles para el tipo seleccionado
            habitaciones_disponibles = Habitacion.objects.filter(
                tipo=tipo_habitacion,
                reserva__fecha_salida__lte=fecha_llegada,
                reserva__fecha_llegada__gte=fecha_salida
            )

            if habitaciones_disponibles.exists():
                raise ValidationError('La habitación no está disponible en las fechas seleccionadas.')

    def clean_tipo_habitacion(self):
        tipo_habitacion = self.cleaned_data.get('tipo_habitacion')

        # Verifica si hay habitaciones disponibles de ese tipo
        habitaciones_disponibles = Habitacion.objects.filter(tipo=tipo_habitacion, reserva__isnull=True)

        if not habitaciones_disponibles:
            raise forms.ValidationError('No hay habitaciones disponibles de este tipo.')

        # Asigna la primera habitación disponible
        return habitaciones_disponibles.first().tipo

    def save(self, commit=True):
        # Obtiene la habitación seleccionada
        tipo_habitacion = self.cleaned_data.get('tipo_habitacion')
        
        # Encuentra la primera habitación disponible de ese tipo
        habitacion_disponible = Habitacion.objects.filter(tipo=tipo_habitacion, reserva__isnull=True).first()
        
        if not habitacion_disponible:
            raise ValueError('No hay habitaciones disponibles de este tipo.')

        # Asigna la habitación seleccionada al objeto Reserva
        self.instance.habitacion = habitacion_disponible
        return super().save(commit)
