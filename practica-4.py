#Practica 4 
import string


semestre = int(input("Ingrese el semestre: "))
diccionario = {}
creditos_totales = 0
i =1
if semestre > 8:
    print("No se puede ingresar un semestre mayor a Octavo")

if semestre > 2 :
    num_materias = 6
else : 
    num_materias = 7

while i < num_materias:
    materia = input("Ingrese la materia: ")
    creditos = int(input("Ingrese los creditos: "))
    creditos_totales += creditos
    diccionario[materia] = creditos
    i += 1

print("Semestre: " + str(semestre)+", Total de creditos: "+ str(creditos_totales))
print(diccionario)
