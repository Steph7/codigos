# _*_coding: utf-8 _*_

import math as m

def hipotenusa(a, b):
    h = m.sqrt(a**2 + b**2)
    return h

# Recebe os valores dos catetos

a = float(input())
b = float(input())

print("%.4f" % hipotenusa(a,b))