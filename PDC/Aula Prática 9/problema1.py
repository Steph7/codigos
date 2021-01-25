# _*_coding: utf-8 _*_

def contarLetrasIguais(palavra):
    d = dict()
    for x in palavra:
        if(x not in d):
            d[x] = 1
        else:
            d[x] = d[x] + 1
    #print(d)
    maior = None
    for x in d:
        if((maior == None) or (d[x] > maior)):
            maior = d[x]
            imprimirMaior = x
    print(imprimirMaior)

palavra = input()

contarLetrasIguais(palavra)