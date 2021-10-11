from django.shortcuts import render, redirect
from .models import Categoria
from .forms import CategoriaForm

# Create your views here.


def indexCategoria(request):
	categoria = Categoria.objects.all()
	return render(request, 'categorias/index.html', {'categorias': categoria})


def createCategoria(request):
	form = CategoriaForm()

	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('indexCate')

	return render(request, 'categorias/create.html', {'forms':form})


def editCategoria(request, id):
	categoria = Categoria.objects.get(id = id)
	if request.method == 'GET':
		form = CategoriaForm(instance = categoria)
	else:
		form = CategoriaForm(request.POST, instance = categoria)
		if form.is_valid():
			form.save()
			return redirect('indexCate')

	return render(request, 'categorias/edit.html', {'forms':form})