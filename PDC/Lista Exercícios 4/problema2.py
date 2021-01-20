# _*_coding: utf-8 _*_

def soma_inteiros(numero):
    x = 0
    soma = 0
    while(x <= numero):
        if(x % 2 == 0):
            soma = soma + x
        x += 1
    return soma

# Receber um número inteiro
n = int(input())

print(soma_inteiros(n))
