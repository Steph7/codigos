# _*_coding: utf-8 _*_

def soma_digitos(numero):
    n = str(numero)
    soma = 0
    for x in n:
        soma = soma + int(x)
    return(soma)

#Recer um número inteiro
n = int(input())

print("%.2f" % soma_digitos(n))