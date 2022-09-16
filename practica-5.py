#Practica 5 
def imprimirFormato(**id):
    for llave, valor in id.items():
            print(f'{llave}:{valor}')

datos = {'Nombre':'Lizandro','Apellido':'Valdez', 'edad':21,'carrera':'ISC','#Control':'18100241'}
imprimirFormato(**datos)