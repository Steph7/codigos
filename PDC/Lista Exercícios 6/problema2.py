# coding: utf-8 _*_

def desenharNumeros(numero):
    listaCompleta = []
    for i in range(1, numero+1):
        subListas = []
        for j in range(0, i):
            subListas.append(str(i))
        for j in range(i, (2*numero - i)):
            subListas.append(' ')
        for j in range(0, i):
            subListas.append(str(i))
        adicionarLinha = ''.join(subListas)
        listaCompleta.append(adicionarLinha)
    for linha in listaCompleta:
        print(linha)


n = int(input())

desenharNumeros(n)