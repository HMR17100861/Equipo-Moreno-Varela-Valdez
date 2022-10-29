"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BienvenidoIndex,name='index'),
    path('cliente',bienvenido,name='cliente'),
    path('detalle_persona/<int:id>',detallePersona),
    path('factura_cliente/<int:id>',facturaCliente),
    path('nueva_persona',nuevaPersona),
    path('editar_persona/<int:id>',editarPersona),
    path('eliminar_persona/<int:id>',eliminarPersona),
    path('orden',bienvenidoC,name='orden'),
    path('detalle_carro/<int:id>',detalleCarro),
    path('nuevo_carro',nuevoCarro),
    path('editar_carro/<int:id>',editarCarro),
    path('eliminar_carro/<int:id>',eliminarCarro),
    path('detalle_factura/<int:id>',facturaCarro),
    path('factura',BienvenidoFacturar,name='factura'),
    path('detalle_factura/<int:id>',detalleFactura),
    path('nueva_factura',nuevaFactura),
    path('editar_factura/<int:id>',editarFactura),
    path('eliminar_factura/<int:id>',eliminarFactura),
    path('entrega',BienvenidoDomicilio,name='entrega'),
    path('detalle_domicilio/<int:id>',detalleDomicilio),
    path('agregar_domicilio',nuevoDomicilio),
    path('editar_domicilio/<int:id>',editarDomicilio),
    path('eliminar_domicilio/<int:id>',eliminarDomicilio),
]
