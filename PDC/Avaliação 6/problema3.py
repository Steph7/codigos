# _*_coding: utf-8 _*_

import math as m

vetorA = []
vetorB = []

dimensaoVetor = int(input("Digite a dimensão: "))
i = 0

while(i < dimensaoVetor):
    x = int(input())
    vetorA.append(x)
    i += 1

i = 0
while(i < dimensaoVetor):
    x = int(input())
    vetorB.append(x)
    i += 1

#print(vetorA)
#print(vetorB)

produtoEscalar = 0

for (x, y) in zip (vetorA, vetorB):
        produtoEscalar = produtoEscalar + (x * y)

print("Produto Escalar: ", produtoEscalar)