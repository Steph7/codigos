# _*_coding: utf-8 _*_

def has_duplicates(lista):
    novaLista = dict()
    contador = 0
    for x in lista:
        if(x not in novaLista):
            novaLista[x] = 1
        else:
            novaLista[x] = novaLista[x] + 1

    #print(novaLista)
    for string in novaLista:
        if novaLista[string] > 1:
            contador += 1
        else:
            continue
    if(contador >= 1):
        return True
    else:
        return False

entrada = input()
lista = entrada.split()

duplicados = has_duplicates(lista)

print(duplicados)