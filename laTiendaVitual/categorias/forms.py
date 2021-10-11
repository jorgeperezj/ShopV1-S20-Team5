from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CategoriaForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs = {
			'class': 'form-control',
		}
	class Meta:
		model = Categoria
		fields = '__all__'