from django.shortcuts import render
from .forms import CategoriaForm, EntradaForm, ComentarioForm, BusquedaForm
from .models import Entrada

def index(request):
    entradas = Entrada.objects.all()
    return render(request, 'index.html', {'entradas': entradas})

def ingresar_entrada(request):
    categoria_form = CategoriaForm()
    entrada_form = EntradaForm()
    comentario_form = ComentarioForm()

    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)
        entrada_form = EntradaForm(request.POST)
        comentario_form = ComentarioForm(request.POST)
        if categoria_form.is_valid() and entrada_form.is_valid() and comentario_form.is_valid():
            categoria_form.save()
            entrada_form.save()
            comentario_form.save()

    return render(request, 'ingresar_entrada.html', {'categoria_form': categoria_form, 'entrada_form': entrada_form, 'comentario_form': comentario_form})

def buscar_entrada(request):
    form_busqueda = BusquedaForm()
    resultados = []

    if request.method == 'POST':
        form_busqueda = BusquedaForm(request.POST)
        if form_busqueda.is_valid():
            termino = form_busqueda.cleaned_data['termino_busqueda']
            resultados = Entrada.objects.filter(titulo__icontains=termino)

    return render(request, 'buscar_entrada.html', {'form_busqueda': form_busqueda, 'resultados': resultados})
