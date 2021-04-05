# _*_coding: utf-8 _*_

def alfabetica(arquivo):
    linhas = arquivo.readlines()
    lista = []
    for x in linhas:
        lista.append(x.strip())

    lista.sort()

    for x in lista:
        print(x)
    exit()