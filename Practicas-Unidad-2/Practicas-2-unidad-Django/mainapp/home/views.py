from http.client import ImproperConnectionState
from django.shortcuts import render
from pydoc import render_doc
from django.shortcuts import render,get_object_or_404,redirect
from home.forms import PersonaForm,CarroForm,FacturaForm,DomicilioForm
from home.models import *


# Create your views here.
def facturaCliente(request,id):
    
    factura = get_object_or_404(Factura,comprador=id)
    return render(request,'detalleFactura.html',{'factura':factura})

def detallePersona(request,id):
    persona = get_object_or_404(Persona,pk=id)
    return render(request,'detallePersona.html',{'persona':persona})

def nuevaPersona(request):
    if request.method == "POST":
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
         formaPersona=PersonaForm
         return render(request,'agregarPersona.html',{'formaPersona':formaPersona})

def editarPersona(request,id):
    persona= get_object_or_404(Persona,pk=id)
    if request.method == 'POST':
        formaPersona= PersonaForm(request.POST,instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance=persona)
        return render(request,'editarPersona.html',{'formaPersona':formaPersona})

def eliminarPersona(request,id):
    persona=get_object_or_404(Persona,pk=id)
    if persona:
        persona.delete()
        return redirect('index')


#EMPEIZAN LAS VISTAS DEL CARRO
def facturaCarro(request,id):
    
    factura = get_object_or_404(Factura,compra=id)
    return render(request,'detalleFactura.html',{'factura':factura})

def detalleCarro(request,id):
    carro = get_object_or_404(Carro,pk=id)
    return render(request,'detalleCarro.html',{'carro':carro})

def nuevoCarro(request):
    if request.method == "POST":
        formaCarro = CarroForm(request.POST)
        if formaCarro.is_valid():
            formaCarro.save()
            return redirect('orden')
    else:
         formaCarro=CarroForm
         return render(request,'agregarCarro.html',{'formaCarro':formaCarro})

def editarCarro(request,id):
    carro= get_object_or_404(Carro,pk=id)
    if request.method == 'POST':
        carroForm= CarroForm(request.POST,instance=carro)
        if carroForm.is_valid():
            carroForm.save()
            return redirect('orden')
    else:
        carroForm = CarroForm(instance=carro)
        return render(request,'editarCarro.html',{'formaCarro':carroForm})

def eliminarCarro(request,id):
    carro=get_object_or_404(Carro,pk=id)
    if carro:
        carro.delete()
        return redirect('orden')

#Agregar Factura
def detalleFactura(request,id):
    
    factura = get_object_or_404(Factura,factura=id)
    return render(request,'detalleFactura.html',{'factura':factura})


def nuevaFactura(request):
    if request.method == "POST":
        formaFactura = FacturaForm(request.POST)
        if formaFactura.is_valid():
            formaFactura.save()
            return redirect('factura')
    else:
         formaFactura=FacturaForm()
         return render(request,'agregarFactura.html',{'formaFactura':formaFactura})

def editarFactura(request,id):
    factura= get_object_or_404(Factura,pk=id)
    if request.method == 'POST':
        formaFactura= FacturaForm(request.POST,instance=factura)
        if formaFactura.is_valid():
            formaFactura.save()
            return redirect('factura')
    else:
        formaFactura = FacturaForm(instance=factura)
        return render(request,'editarFactura.html',{'formaFactura':formaFactura})

def eliminarFactura(request,id):
    factura=get_object_or_404(Factura,pk=id)
    if factura:
        factura.delete()
        return redirect('BienvenidoFactura.html')

## empiezan las vistas del domicilio
def detalleDomicilio(request,id):
    domicilio = get_object_or_404(Domicilio,pk=id)
    return render(request,'detalleDomicilio.html',{'domicilio':domicilio})


def nuevoDomicilio(request):
    if request.method == "POST":
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('BienvenidoDomicilio.html')
    else:
         formaDomicilio=DomicilioForm()
         return render(request,'agregarDomicilio.html',{'formaDomicilio':formaDomicilio})

def editarDomicilio(request,id):
    domicilio=get_object_or_404(Domicilio,pk=id)
    if request.method == "POST":
        
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('editarDomicilio.html')
    else:
         formaDomicilio=DomicilioForm(instance=domicilio)
         return render(request,'editarDomicilio.html',{'formaDomicilio':formaDomicilio})

def eliminarDomicilio(request,id):
    domicilio=get_object_or_404(Domicilio,pk=id)
    if domicilio:
        domicilio.delete()
        return redirect('BienvenidoDomicilio.html')
