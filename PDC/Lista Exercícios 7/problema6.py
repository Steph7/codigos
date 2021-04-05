# _*_coding: utf-8 _*_

def maior_menor(arquivo):
    linhas = arquivo.readlines()
    lista =[]
    for x in linhas:
        lista.append(x.strip())
    d = dict()
    contador = 0
    aux = "" 
    for x in lista:
        if(contador == 0) or (contador % 2 == 0):
            d[x] = None
            aux = x
        else:
            d[aux] = int(x)
        contador += 1
    
    maisNovo = min(d, key=d.get)
    maisVelho = max(d, key=d.get)
    print(maisNovo)
    print(maisVelho)