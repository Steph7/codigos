# _*_coding: utf-8 _*_
import math

def verifica_triangulo(lado1, lado2, lado3):
    if lado1 < lado2 + lado3:  #and abs(lado2 - lado3) < lado1:
        if lado2 < lado1 + lado3: #and abs(lado1 - lado3) < lado2:
            if lado3 < lado1 + lado2: #and abs(lado1 - lado2) < lado3:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    exit()

def tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        print('Equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Isósceles')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('Escaleno')
    exit()


#RECEBE valores para os lados 
x = int(input("Digite o valor do primeiro lado: "))
y = int(input("Digite o valor do segundo lado: "))
z = int(input("Digite o valor para o terceiro lado: "))

#Verifica se é um triângulo a partir das funções criadas
verifica = verifica_triangulo(x, y, z)

if verifica == True:
    tipo = tipo_triangulo(x, y, z)
else:
    print('Não forma triângulo')
    exit()