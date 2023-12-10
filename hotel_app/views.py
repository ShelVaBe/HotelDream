from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .forms import ReservaForm
from django.contrib import messages
#def reservar_view(request):
 #   return render(request, 'Reservar.html')
def reservacion(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save()
            messages.success(request, '¡Reserva realizada con éxito!')
            return redirect('reservacion')  # Redirige de nuevo a la misma vista
    else:
        form = ReservaForm()

    return render(request, 'Reservar.html', {'form': form})






