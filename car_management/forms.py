from django import forms
from .models import Car

class CarForm(forms.ModelForm):
	class Meta:
		model = Car
		fields = ['brand', 'model', 'rental_price_per_day', 'availability', 'image']
		widgets = {
			'availability': forms.CheckboxInput(),
		}