# _*_coding: utf-8 _*_

import math as m

def bhaskara(a, b, c):
    delta = b**2 - (4*a*c)
    if(a == 0) or (delta < 0):
        print('(None, None)')
        exit()
    sdelta = m.sqrt(delta)
    raiz1 = float((-b + sdelta)/2*a)
    raiz2 = float((-b - sdelta)/2*a)
    print("%.1f, %.1f" % (raiz1, raiz2))
    exit()


a = int(input())
b = int(input())
c = int(input())

bhaskara(a, b, c)