# _*_coding: utf-8 _*_

import math as m

def volume_esfera(raio):
    volume = (4/3) * m.pi * raio **3
    print('resultado', "%.4f" % volume)

#Receber o valor do raio da esfera 
r = float(input())
volume_esfera(r)
