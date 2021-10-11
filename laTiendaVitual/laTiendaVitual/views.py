#Views de pruebas

from django.shortcuts import render

def presentacion(request):
	return render(request, 'presentacion.html')