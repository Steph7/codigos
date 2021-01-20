# _*_coding: utf-8 _*_

lado1 = float(input())
lado2 = float(input())
lado3 = float(input())

if(lado1 < lado2 + lado3):
    if(lado2 < lado1 + lado3):
        if(lado3 < lado1 + lado2):
            r = True
        else:
            r = False
    else:
        r = False
else:
    r = False

if(r == False):
    print('Não forma triângulo')

if(r == True):
    if(lado1 == lado2) and (lado2 == lado3):
        print('Equilátero')
    elif(lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
        print('Isósceles')
    elif(lado1 != lado2) and (lado1 != lado3) and (lado2 != lado3):
        print('Escaleno')
