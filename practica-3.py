#Practica 3
nombre = input("Introduce tu nombre: ")
nombre_invertido = ""
for letra in nombre:
    nombre_invertido = letra + nombre_invertido
for letra in nombre_invertido:
    print(letra)