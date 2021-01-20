# _*_coding: utf-8 _*_

def fatorial(numero):
    x = 1
    fatorial = 1
    while(x <= numero):
        fatorial = fatorial * x
        x += 1
    return fatorial




# Receber um número inteiro do usuário
n = int(input())

print(fatorial(n))