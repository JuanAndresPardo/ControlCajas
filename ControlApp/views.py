from django.shortcuts import render, redirect
from .forms import MonedaForm, BancoLibradorForm, ChEmitidos, ChRecibidos



# Create your views here.

def agregar_moneda(request):
    if request.method == 'POST':
        form = MonedaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ruta_donde_redirigir_despues_de_agregar_moneda')
    else:
        form = MonedaForm()
    return render(request, 'template.html', {'form': form})

def agregar_banco_librador(request):
    if request.method == 'POST':
        form = BancoLibradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ruta_donde_redirigir_despues_de_agregar_banco_librador')
    else:
        form = BancoLibradorForm()
    return render(request, 'template.html', {'form': form})

