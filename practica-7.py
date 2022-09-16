#7 Formateo y conversiones
# Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir 
# YYYY/MM/DD” la segunda “2.- Imprimir MM/DD/YYYY” una vez seleccionada la opción imprimir la fecha 
# del día de hoy en el formato seleccionado.
from datetime import datetime

f=input("Que formato de hora quieres imprimir 1.-(YYYY/MM,DD), 2.-(MM/DD/YYYY)")
fecha= datetime.now()
if f==1:
    format=fecha.strftime("%Y/%m/%d")
    print(format)
else:
    format=fecha.strftime("%m/%d/%Y")
    print(format)
