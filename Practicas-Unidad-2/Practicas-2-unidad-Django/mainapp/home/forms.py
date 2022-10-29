
from django.forms import ModelForm,EmailInput
from home.models import *
class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields= '__all__'
        widgets={
            'email': EmailInput(attrs={'type':'email'})
        }

class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields= '__all__'

class FacturaForm(ModelForm):
    class Meta:
        model = Factura
        fields= '__all__'

class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields= '__all__'
