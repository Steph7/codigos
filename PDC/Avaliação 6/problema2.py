# _*_coding: utf-8 _*_

import math as m

lista = []
i = 0

while(i < 10):
    n = int(input())
    lista.append(n)
    i += 1

soma = 0
for x in lista:
    soma = soma + x

media = soma/10

somatorio = 0

for x in lista:
    y = (x - media)**2
    somatorio = somatorio + y

multiplicador = (1/(10 - 1))

desvioPadrao = m.sqrt(somatorio * multiplicador)

print("Desvio Padrão: ", "%.2f" % desvioPadrao)