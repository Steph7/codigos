# _*_coding: utf-8 _*_
import math as m

num = float(input("Digite um número: "))

if(num >= 0):
    print("%.3f" % m.sqrt(num))

if (num < 0):
    print('Número inválido')
