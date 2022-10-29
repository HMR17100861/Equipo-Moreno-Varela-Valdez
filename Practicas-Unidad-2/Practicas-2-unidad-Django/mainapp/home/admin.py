from django.contrib import admin
from home.models import Persona,Carro,Domicilio,Factura

# Register your models here.
admin.site.register(Persona)
admin.site.register(Domicilio)
admin.site.register(Carro)
admin.site.register(Factura)