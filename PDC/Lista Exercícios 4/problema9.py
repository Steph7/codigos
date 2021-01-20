# _*_coding: utf-8 _*_

lista = []

while True:
    numero = int(input())
    
    if numero == 0:
        break
    
    lista.append(numero)

n = 0
soma = 0
nprimos = 0

for i in lista:
    primo = True
    
    if i % 2 == 0:
        soma += i
        n += 1
    
    if i <= 1:
        primo = False

    for j in range(2,i):
        if i % j == 0:
            primo = False
            break

    if primo == True:
        nprimos += 1
        

print('A soma é:', sum(lista))
print('O maior número é:', max(lista))
print('O menor número é:', min(lista))
print('A média dos pares é:', soma/n)
print('O número de primos é:', nprimos)