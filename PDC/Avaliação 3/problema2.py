# _*_coding:utf-8 _*_

# Considerando a distância percorrida em km
# e a quantidade de litros de gasolina
def consumo(dist_percorrida, quant_litros):
    km_litros = dist_percorrida / quant_litros

    if(km_litros < 8):
        print("Venda o carro!")
    elif(km_litros >= 8) and (km_litros < 12):
        print("Econômico!")
    elif(km_litros >= 12):
        print("Super Econômico!")
    exit()

dist = int(input("Distância Percorrida: "))
litros = float(input("Litros de gasolina: "))


consumo(dist, litros)