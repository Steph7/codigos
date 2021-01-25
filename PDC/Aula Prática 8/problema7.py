# _*_coding: utf-8 _*_

def imprime_naturais_impares(numero):
    if(numero % 2 != 0):
        print(numero)
    while(numero >= 1):
        imprime_naturais_impares(numero-1)
    exit()
            
        
n = int(input("Digite N: "))

imprime_naturais_impares(n)