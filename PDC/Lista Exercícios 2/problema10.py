# _*_coding: utf-8 _*_

# Distância em KM
distancia = float(input())

# Quantidade de gasolina em L
litros = float(input())

# Consumo em km/L
consumo = distancia/litros

if consumo < 8:
    print('Venda o carro!')
if consumo >= 8 and consumo <= 12:
    print('Econômico!')
if consumo > 12:
    print('Super Econômico!')
