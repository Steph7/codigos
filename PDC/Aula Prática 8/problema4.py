# _*_coding: utf-8 _*_

def soma(numero):
    if(numero == 1):
        return numero
    else:
        while(numero > 1):
            return numero + soma(numero-1)

n = int(input("Digite N: "))

soma = soma(n)
print(soma)
