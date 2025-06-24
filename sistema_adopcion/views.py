from django.shortcuts import render, redirect
from django import forms 
from .models import Perro


class formPerro(forms.ModelForm):
    class Meta:
        model = forms.ModelForm
        fields = '__all__'

def agregar_perro(request):
    if request.method == 'POST':
        form = formPerro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_perros')
    else:
        form = formPerro()
    return render(request, 'agregar_perro.html', {'form': form})
