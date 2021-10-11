from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProductoForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs = {
			'class': 'form-control',
		}
		self.fields['cantidad'].widget.attrs = {
			'class': 'form-control',
			'value': 0
		}
		self.fields['estado'].widget.attrs = {
			'class': 'form-control',
			'value': 0
		}
		self.fields['categoria'].widget.attrs = {
			'class': 'form-control',
		}


	class Meta:
		model = Producto
		fields = '__all__'