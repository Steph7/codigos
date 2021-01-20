# _*_coding: utf-8 _*_

n1 = int(input("Digite o primeiro inteiro: "))
n2 = int(input("Digite o segunto inteiro: "))
n3 = int(input("Digite o terceiro inteiro: "))
n4 = int(input("Digite o quarto inteiro: "))
n5 = int(input("Digite o quinto inteiro: "))

array = [n1, n2, n3, n4, n5]

max = None
min = None

quant = 0

#Definindo o maior número
for x in array:
   if max is None or x > max:
        max = x
print('Maior: ', max)

#Definindo o menor número
for x in array:
    if min is None or x < min:
        min = x
print('Menor: ', min)

#Verificando se o número é divisível por 3
for x in array:
    if x % 3 == 0:
        quant += 1
print('Quantidade de divisíveis por 3: ', quant)
