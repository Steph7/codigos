# _*_coding: utf-8 _*_

def calcula_valor(preço_litro, quant_litro, tipo_combustivel):
    if tipo_combustivel == 'a':
        if quant_litro <= 20:
            desconto = 0.03 
        elif quant_litro > 20:
            desconto = 0.05
    elif tipo_combustivel == 'g':
        if quant_litro <= 20:
            desconto = 0.04
        elif quant_litro > 20:
            desconto = 0.06
    
    valor_liq = (preço_litro * quant_litro) * (1 - desconto)

    print('Total: ', "%.2f" % valor_liq)
    exit()


quantidade = float(input("Digite a quantidade de litros: "))
tipo = input('Digite o tipo de combustível: ')
preco = float(input("Digite o preço do litro de combustível: "))

calcula_valor(preco, quantidade, tipo)