from django import forms
from .models import Perro

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = '__all__'
