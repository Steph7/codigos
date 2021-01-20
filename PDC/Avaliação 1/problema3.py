#_*_coding: utf-8 _*_

numero = str(input('Digite um inteiro de 4 algarismos: '))
# print(numero)

soma = 0

for x in numero:
    soma += int(x)
print("Resultado: ", soma)
