# _*_coding: utf-8 _*_

def encontrarMultiplos(numero):
    multiplosNumero = []
    for i in range(1, numero+1):
        if(numero % i == 0):
            multiplosNumero.append(i)
    return multiplosNumero

def calcularMDC(lista1, lista2):
    maior = None
    multiplosComuns = []
    for x in lista1:
        for y in lista2:
            if x == y:
                multiplosComuns.append(x)
    
    for x in multiplosComuns:
        if maior == None or x > maior:
            maior = x
    return maior



n1 = int(input())
n2 = int(input())

m1 = encontrarMultiplos(n1)
m2 = encontrarMultiplos(n2)

print(calcularMDC(m1, m2))
