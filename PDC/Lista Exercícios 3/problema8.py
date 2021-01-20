# _*_coding: utf-8 _*_

def peso_ideal(altura, sexo):
    if sexo == 'F':
        peso = (62.1 * altura) - 44.7
    if sexo == 'M':
        peso = (72.7 * altura) - 58
    return peso

#Altura (em metros)
a = float(input())

#Sexo: F - feminino e M - masculino
s = input()

print("%.2f" % peso_ideal(a, s))
