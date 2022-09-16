#2 Manejo y manipulación de elementos de una lista
#Escribir un programa que almacene el abecedario en una lista, elimine de 
# la lista las letras que ocupen 
#posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
# print (string.ascii_uppercase)
from copy import deepcopy
from re import A
import string
#Abecedario= {
 #       'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26
  #  } 
#Abecedario=dict([(1,'A'),(2,'B'),(3,'C'),(4,'D'),(5,'E'),(6,'F'),(7,'G'),(8,'H'),(9,'I'),(10,'J'),(11,'K'),(12,'L'),(13,'M'),(14,'N'),(15,'O'),(16,'P'),(17,'Q'),(18,'R'),(19,'S'),(20,'T'),(21,'U'),(22,'V'),(23,'W'),(24,'X'),(25,'Y'),(26,'Z'),])
#se declara funcion para ver si es divisible en 3
# def esDivisibleX3(V):
#     if(v % 3)==0:
#         Abecedario.pop(v)
Abecedario=list(string.ascii_lowercase)
#print(Abecedario)
# print(Abecedario.keys())
# print(Abecedario.values())
nAbecedario=deepcopy(Abecedario)

#IMPRIMIMOS LOS VALORES DEL DICCIONARIO
bandera=2
for x in Abecedario:
   
    
    
    if(bandera<18):
        l=bandera
        nAbecedario.pop(l)
        bandera=bandera+2
       
    
    else:
        break
    
#Abecedario=list(string.ascii_uppercase)
print(Abecedario)
print(nAbecedario)

# for valor in map(Abecedario):
#     if(valor % 3) ==0:
#         Abecedario.popitem(valor)


# x=2
# for x in len(Abecedario):
    
#         Abecedario.pop(x)
#         x+3
# print(Abecedario)

