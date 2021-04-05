# _*_coding: utf-8 _*_

def encontrarMultiplos(numero):
    listaMultiplos = []
    for i in range(1, numero+1):
        if(numero % i == 0):
            listaMultiplos.append(i)
    return listaMultiplos

def compararListas(lista):
    A = set(lista[0])
    B = set(lista[1])
    C = set(lista[2])
    D = set(lista[3])

    intAB = set(A.intersection(B))
    intCD = set(C.intersection(D))
    intABCD = intAB.intersection(intCD)

    maior = None
    for x in intABCD:
        if maior == None or x > maior:
            maior = x
    return maior



def mdc4(arquivo):
    listaNumeros = []
    listasMultiplostodos = []
    for linha in arquivo:
        for numero in linha.split():
            listaNumeros.append(int(numero))
    for x in listaNumeros:
        y = encontrarMultiplos(x)
        listasMultiplostodos.append(y)
    print(compararListas(listasMultiplostodos))
