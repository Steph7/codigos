# _*_coding: utf-8 _*_

def encontrarMaior(lista):
    listaSeparada = lista.split()
    maior = None
    for x in listaSeparada:
        n = len(x)
        if(maior == None) or (n > maior):
            maior = n
    print(maior)


lista = input()
encontrarMaior(lista)