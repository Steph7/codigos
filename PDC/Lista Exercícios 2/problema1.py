#_*_coding: utf-8 _*_

numero = float(input("Digite um número: "))

# Testar se o número é positivo
if numero > 0:
    numero = numero ** (1/2)
    print("%.3f" % numero)

# Testar se o número é negativo
if numero < 0:
    print('Número inválido')