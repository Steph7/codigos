# _*_coding: utf-8 _*_

d = dict()

while True:
    idade = int(input())
    nome = input()
    if idade < 0:
        break
    d[nome] = idade

max = max(d, key=d.get)
min = min(d, key=d.get)


print(min)
print(max)
