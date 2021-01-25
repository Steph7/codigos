# _*_coding: utf-8 _*_

def imprime_naturais_pares(numero):
    if(numero != 0):
        imprime_naturais_pares(numero-1)
    if((numero % 2 == 0) or (numero == 0)):
        print(numero)
        
n = int(input("Digite N: "))

imprime_naturais_pares(n)