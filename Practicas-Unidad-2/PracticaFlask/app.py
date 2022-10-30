
from flask import Flask,request,url_for,render_template,redirect
from database import db
from flask_migrate import Migrate
from models import EmpresaTrabajo, Oficio, Persona
from forms import EmpresaForm, OficioForm, PersonaForm


app = Flask(__name__)


#CONFIGURACION DE LA BASE DE DATOS 
USER_DB = 'postgres'
PASS_DB = '12345'
URL_DB = 'localhost'
NAME_DB='flask_prac'
FULL_URL= f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

#CONFIGURACION DE MIGRACION

migrate = Migrate()
migrate.init_app(app,db)

#FORM
app.config["SECRET_KEY"]="una llave muy secreta"


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    personas = Persona.query.all()
    return render_template('index.html',personas=personas)

@app.route('/ver/<int:id>')
def verDetalle(id):
    persona = Persona.query.get_or_404(id)
    return render_template('detalle.html',persona=persona)

@app.route('/agregar', methods=['GET','POST'])
def agregar():
    persona = Persona()
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            #insert
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregar.html',forma=personaForm)

@app.route('/Oficio', methods=['GET','POST'])
def agregarOficio():
    oficio = Oficio()
    oficioForm = OficioForm(obj=oficio)
    if request.method == 'POST':
        if oficioForm.validate_on_submit():
            oficioForm.populate_obj(oficio)
            #insert
            db.session.add(oficio)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarOficio.html',forma=oficioForm)



@app.route('/Empresa', methods=['GET','POST'])
def agregarEmpresa():
    empresa = EmpresaTrabajo()
    empresaForm = EmpresaForm(obj=empresa)
    if request.method == 'POST':
        if empresaForm.validate_on_submit():
            empresaForm.populate_obj(empresa)
            #insert
            db.session.add(empresa)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarOficina.html',forma=empresaForm)




@app.route('/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    persona = Persona.query.get_or_404(id)
    personaForm = PersonaForm(obj=persona)
    if request.method == "POST":
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editar.html',forma=personaForm)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('inicio'))