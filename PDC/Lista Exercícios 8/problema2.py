# _*_coding: utf-8 _*_

import math as m

def raio_circ(area):
    pi = 3.14
    # FÓRMULA: área = pi * (raio**2)
    raio = m.sqrt(area / pi)
    perimetro = 2 * pi * raio
    #trecho adicionado por 
    #falha na correção (número de casas decimais da resposta)
    if(raio == 0):
        print ("(%d, %d)" % (raio, perimetro))
    else:
        print ("(%.1f, %.2f)" % (raio, perimetro))
    exit()


area = float(input())
raio_circ(area)
