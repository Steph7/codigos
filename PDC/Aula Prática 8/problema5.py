# _*_coding: utf-8 _*_

def imprime_naturais(numero):
    if(numero != 0):
        imprime_naturais(numero-1)
    print(numero)
        
n = int(input("Digite N: "))

imprime_naturais(n)