# _*_coding: utf-8 _*_

def sinal(numero):
    if numero == 0:
        return 0
    if numero < 0:
        return -1
    if numero > 0:
        return 1
    exit()


n = int(input())

print('resultado', sinal(n))