# _*_coding: utf-8 _*_

def ordenarNomes(nome1, nome2, nome3):
    listaOrdenada = []

    if nome1 < nome2 and nome1 < nome3:
        listaOrdenada.append(nome1)
        if nome2 < nome3:
            listaOrdenada.append(nome2)
            listaOrdenada.append(nome3)
        else:
            listaOrdenada.append(nome3)
            listaOrdenada.append(nome2)
    elif nome2 < nome1 and nome2 < nome3:
        listaOrdenada.append(nome2)
        if nome2 < nome3:
            listaOrdenada.append(nome1)
            listaOrdenada.append(nome3)
        else:
            listaOrdenada.append(nome3)
            listaOrdenada.append(nome1)
    else:
        listaOrdenada.append(nome3)
        if nome2 < nome3:
            listaOrdenada.append(nome2)
            listaOrdenada.append(nome1)
        else:
            listaOrdenada.append(nome1)
            listaOrdenada.append(nome2)
    
    for x in listaOrdenada:
        print(x)

n1 = input()
n2 = input()
n3 = input()

ordenarNomes(n1, n2, n3)