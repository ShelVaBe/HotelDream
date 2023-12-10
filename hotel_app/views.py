from django.shortcuts import render,redirect,  get_object_or_404
from django.http import HttpResponse, JsonResponse
from .forms import ReservaForm
from .models import Reserva
from django.contrib import messages
#def reservar_view(request):
 #   return render(request, 'Reservar.html')
def reservacion(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save()
            messages.success(request, '¡Reserva realizada con éxito!')
            return redirect('reservacion_exitosa', reserva_id=reserva.id)
    else:
        form = ReservaForm()

    return render(request, 'Reservar.html', {'form': form})

def reservacion_exitosa(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    return render(request, 'ReservacionExitosa.html', {'reserva': reserva})




