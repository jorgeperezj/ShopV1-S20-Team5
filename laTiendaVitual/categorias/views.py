from django.shortcuts import render, redirect
from .models import Categoria
from .forms import CategoriaForm

# Create your views here.


def indexCategoria(request):
	# Listar las categorías en el index y el formulario
	categoria = Categoria.objects.all()
	form = CategoriaForm()

	# Método de guardar la categoría
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	
	return render(request, 'categorias/index.html', {'categorias': categoria, 'forms': form})


def editarCategoria(request, id):
	categoria = Categoria.objects.get(id = id)
	formEdit = CategoriaForm(instance = categoria)
	contexto = {
		'formEdit': formEdit
	}
	return render(request, 'categorias/edit.html', formEdit)