import math


def osztok(szam):
    lista = []
    for index in range(2,round(math.sqrt(szam)+1)):
        if szam % index == 0:
            lista.append(index)
        return lista
    print(osztok(10007))


def kiir(lista):
    print(lista)

def osztok2(szam):
    lista = []
    oszto = 2
    while oszto <= math.sqrt(szam):
        if szam % oszto == 0:
            lista.append(oszto)
        oszto += 1
    return lista
