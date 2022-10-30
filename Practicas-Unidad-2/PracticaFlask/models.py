from app import db

class Persona(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    direccion = db.Column(db.String(250))
   
   

    def __str__(self) -> str:
        return(f'ID:{self.id},'
        f'Nombre:{self.nombre},'
        f'Apellido:{self.apellido},'
        f'Direccion:{self.direccion}')

class Oficio(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    ocupacion = db.Column(db.String(250))
    sueldo = db.Column(db.String(250))


    def __str__(self) -> str:
        return(f'ID:{self.id},'
        f'Ocupacion:{self.ocupacion},'
        f'Sueldo:{self.sueldo}')

class EmpresaTrabajo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombremepresa = db.Column(db.String(250))
    direccion = db.Column(db.String(250))


    def __str__(self) -> str:
        return(f'ID:{self.id},'
        f'NombreEmpresa:{self.nombremepresa},'
        f'Direccion:{self.direccion}')

