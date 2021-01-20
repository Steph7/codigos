#_*_coding: utf-8 _*_

#_*_coding: utf-8 _*_

raio = float(input('Digite o valor do raio da circunferência: '))
# print(raio)

pi = 3.1415

perimetro = 2.0 * pi * raio
print('Perímetro: ')
print( "%.2f" % float(perimetro))

area = pi * raio ** 2.0
print('Área: ')
print( "%.2f" % float(area))

volume = 4.0/3.0 * pi * raio ** 3.0
print('Volume: ')
print( "%.2f" % float(volume))