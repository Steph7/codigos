# _*_coding: utf-8 _*_

def consumo(distancia, litros):
    # Consumo em km/L
    consumo = distancia/litros

    if consumo < 8:
        print('Venda o carro!')
    if consumo >= 8 and consumo <= 12:
        print('Econômico!')
    if consumo > 12:
        print('Super Econômico!')
    exit()



# Distância em KM
dist = float(input())

# Quantidade de gasolina em L
l = float(input())

consumo(dist, l)
