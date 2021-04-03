# _*_coding: utf-8 _*_

def removerCaractere(lista, caractere):
    novaLista = []
    for x in lista:
        if(x[0] != caractere):
            novaLista.append(x)
    novaLista = ' '.join(novaLista)
    print(novaLista)
    exit()

l = input().split()
c = input()

removerCaractere(l, c)