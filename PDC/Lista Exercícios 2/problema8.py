# _*_coding: utf-8 _*_

#Receber dados do usuário 
#Altura em metros
altura = float(input())
#Digitar F para Feminino e M para Masculino
sexo = input()

if sexo == 'F':
    peso = (62.1 * altura) - 44.7
elif sexo == 'M':
    peso = (72.7 * altura) - 58

print("%.2f" % peso)
