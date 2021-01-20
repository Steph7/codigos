# _*_coding: utf-8 _*_

def divisores(num1, num2):
    resto = None
    while (resto != 0):
        resto = num1 % num2
        num1 = num2
        num2 = resto
    return num1


def mdc4(a, b, c, d):
    x = divisores(a, b)
    y = divisores(c, d)
    z = divisores(x, y)
    return z

#Receber valores do usuário

valor1 = int(input())
valor2 = int(input())
valor3 = int(input())
valor4 = int(input())

print(mdc4(valor1, valor2, valor3, valor4))