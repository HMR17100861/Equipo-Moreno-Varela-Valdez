from re import S
from unittest import result


# l=list(input('inserte los numeros que desea multiplicar : '))
# l.extend(input('inserte un numero que quiera multiplicar separados por una coma'))

l=list((input('inserte los numeros que desea multiplicar : ')))
while ','in l:
    l.remove(',')
multiL = list(map(int, l))# La funcion 'map' vuelve una lista de tipo str a int


def multiplicarLista(multiL):
    result=1
    for x in multiL:
        result = result * x
    return result

print(multiplicarLista(multiL))