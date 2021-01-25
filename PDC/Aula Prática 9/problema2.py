# _*_coding: utf-8 _*_

def contarLetrasIguais(palavra):
    d = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
    for x in palavra:
        if(x in d):
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