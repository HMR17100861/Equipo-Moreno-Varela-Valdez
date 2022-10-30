
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import DataRequired


class PersonaForm(FlaskForm):
    nombre=StringField('Nombre',validators=[DataRequired()])
    apellido = StringField('Apellido')
    direccion = StringField('Direccion',validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class OficioForm(FlaskForm):
   
    ocupacion = StringField('Ocupacion')
    sueldo = StringField('Sueldo',validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class EmpresaForm(FlaskForm):
   
    nombre = StringField('Nombre')
    direccion = StringField('Direccion',validators=[DataRequired()])
    enviar = SubmitField('Enviar')