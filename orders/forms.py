from django import forms
from django.forms import ModelForm

from .models import Order, Pizza


class OrderForm(ModelForm):

    class Meta:
        model = Pizza
        fields = '__all__'
        # fields = ['cost']
        # exclude = None
        widgets = {
            'crust': forms.RadioSelect(),
            'toppings': forms.CheckboxSelectMultiple(),
            }
