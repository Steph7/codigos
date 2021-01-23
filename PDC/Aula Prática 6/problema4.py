# _*_coding: utf-8 _*_

listaTemperaturas = []
quantidadeEntradas = 12
x = 0
soma = 0
media = 0
while (x < 12):
    temperatura = int(input())
    listaTemperaturas.append(temperatura)
    soma = soma + temperatura
    x += 1
media = soma / 12
print("Média: ", "%.2f" % media)

for n in listaTemperaturas:
    if(n > media):
        print(n)