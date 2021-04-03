# _*_coding: utf-8 _*_

lista = []

while True:
    i = int(input())
    if (i == -1):
        break
    lista.append(i)
    lista = sorted(lista)
    print(lista)
