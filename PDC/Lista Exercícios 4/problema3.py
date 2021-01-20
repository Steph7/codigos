# _*_coding: utf-8 _*_

#Receber valores até que o valor seja zero
soma = 0
quant = 0
while True:
    n = int(input())

    if(n > 0):
        soma = soma + n
        quant += 1
    elif(n < 0):
        continue
    elif(n == 0):
        break

media = soma/quant
print(media)