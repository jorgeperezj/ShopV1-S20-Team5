from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.


def indexProductos(request):
	producto = Producto.objects.all()
	return render(request, 'productos/index.html', {'productos': producto})


def createProducto(request):
	form = ProductoForm()

	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('indexPro')

	return render(request, 'productos/create.html', {'forms':form})


def editProducto(request, id):
	producto = Producto.objects.get(id = id)
	if request.method == 'GET':
		form = ProductoForm(instance = producto)
	else:
		form = ProductoForm(request.POST, instance = producto)
		if form.is_valid():
			form.save()
			return redirect('indexPro')

	return render(request, 'productos/edit.html', {'forms':form})