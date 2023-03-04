from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')
def contacto(request):
    return render(request, 'paginas/contacto.html')
def lista(request):
    clientes = Cliente.objects.all()
    #print(clientes)
    return render(request, 'crud/listar.html',{'clientes':clientes})
