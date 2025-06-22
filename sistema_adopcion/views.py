from django.shortcuts import render, redirect
from .forms import PerroForm

def agregar_perro(request):
    if request.method == 'POST':
        form = PerroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_perros')
    else:
        form = PerroForm()
    return render(request, 'agregar_perro.html', {'form': form})
