# _*_coding: utf-8 _*_

def soma_divisores(numero):
    x = 1
    soma = 0
    while(x < numero):
        if(numero % x == 0):
            soma = soma + x
        x += 1
    return soma


n = int(input("Digite um número: "))

soma = soma_divisores(n)

print('Resultado: ', soma)