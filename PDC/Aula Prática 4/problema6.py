# _*_coding: utf-8 _*_

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Receber um inteiro do usuário
numero = int(input("Digite um inteiro: "))

print(fibonacci(numero))

