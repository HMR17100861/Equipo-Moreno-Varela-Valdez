import os
#8.1=========================
class Usuario:
    def __init__(self, usuario, password,rol, nombre, curp, ciudad) -> None:
        self.usuario = usuario
        self.password = password
        self.rol = rol
        self.nombre = nombre
        self.curp = curp 
        self.ciudad = ciudad
    def __str__(self) -> str:
        return f'Usuario: {self.usuario}, {self.password}, {self.rol}, {self.nombre}, {self.curp}, {self.ciudad}'
#8.1=========================

#8.2=========================
usuarios = []
miUsuario = Usuario("Coty","pass","administrador","Lizandro", "KJADSS", "Nvo Lrdo") #8.3
usuarios.append(miUsuario)
def Registro():
    usuario_r = input("Ingrese su usuario para el registro: ")
    password = input("Ingrese su contraseña para el registro: ")
    nombre = input("Ingrese su nombre para el registro: ")
    curp = input("Ingrese su CURP para el registro: ")
    ciudad = input("Ingrese su ciudad para el registro: ")
    agrega = '1'

    for usuario in usuarios:
        if curp == usuario.curp:
            input("Este curp ya esta registrado")
            agrega = '0'

    if agrega == '1':
        miUsuario = Usuario(usuario_r,password,"cliente",nombre, curp, ciudad)
        usuarios.append(miUsuario)
        input("Te has registrado exitosamente\n")
    os.system ("cls") 

def IniciarSesion():
    usuario_ini_ses = input("Ingrese su usuario: ")
    password_inis_ses = input("Ingrese su contraseña: ")
    os.system ("cls") 
    encontrado = "1"
    for usuario in usuarios:
        #8.3
        if usuario_ini_ses == usuario.usuario and password_inis_ses == usuario.password and usuario.rol =="administrador":
            for usuario in usuarios:
                print(usuario)
            encontrado = "1"
            break
        else: 
            if usuario_ini_ses == usuario.usuario and password_inis_ses == usuario.password:
                print(f'Nombre: {usuario.nombre}\nCURP: {usuario.curp}\nCiudad: {usuario.ciudad}')  
                encontrado = "1"
                break
            else:
                encontrado = "0"
    if encontrado == "0":
        print ("Datos incorrectos")
    input()
    os.system ("cls") 

respuesta = "0"
while respuesta != "3" :
    respuesta = input("Elija una opcion \n1.-Registrarse\n2.-Iniciar Sesión \n3.-Salir\n")
    if respuesta in ("1","2","3"):
        match respuesta: 
            case "1":
                Registro()
                
            case "2":
                IniciarSesion()
    else:
        print("Ingrese una de las opciones correctas")
        input()
        os.system ("cls")
os.system ("cls")   
#8.2=========================