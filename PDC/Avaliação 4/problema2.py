# _*_coding: utf-8 _*_

def numeroHarmonico(numero):
    x = 1
    soma = 0
    while (x <= numero):
        soma = soma + 1/x
        x += 1
    return soma

n = int(input("Digite n: "))

harmonico = numeroHarmonico(n)

print('Resultado: ', "%.2f" % harmonico)