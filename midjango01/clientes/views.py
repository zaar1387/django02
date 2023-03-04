from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente
from .forms import ClientesForm

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')
def contacto(request):
    return render(request, 'paginas/contacto.html')
def lista(request):
    clientes = Cliente.objects.all()
    #print(clientes)
    return render(request, 'crud/listar.html',{'clientes':clientes})
def eliminar(request, idr):
    clienteid = Cliente.objects.get(id=idr)
    clienteid.delete()
    return redirect('lista')
def crear(request):
    formulario = ClientesForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('lista')
    return render(request, 'crud/add.html',{'formulario':formulario})
def editar(request, idr):
    clienteid = Cliente.objects.get(id=idr)
    formulario = ClientesForm(request.POST or None, request.FILES or None, instance=clienteid)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('lista')
    return render(request, 'crud/editar.html',{'formulario':formulario})