import re
from django.shortcuts import render
from home.models import *



# Create your views here.
def bienvenido(request):
    persona = Persona.objects.order_by('id')
   
    return render(request, 'Bienvenido.html',{'persona': persona})

def bienvenidoC(request):
     carro=Carro.objects.order_by('id')
     return render(request, 'BienvenidoOrden.html',{'carro': carro})

def BienvenidoIndex(request):
    return render(request,'index.html')

def BienvenidoFacturar(request):
    factura=Factura.objects.order_by('id')
    return render(request,'BienvenidoFactura.html',{'factura':factura})

def BienvenidoDomicilio(request):
    domicilio=Domicilio.objects.order_by('id')
    return render(request,'BienvenidoEntrega.html',{'domicilio':domicilio})