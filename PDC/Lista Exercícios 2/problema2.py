#_*_coding: utf-8 _*_

custo_consumidor = float(input("Digite o custo de fábrica: "))

# Se o custo de fábrica for inferior a R$ 12.000,00
if custo_consumidor <= 12000.00:
    custo_final_1 = custo_consumidor * 1.05
    print("Custo Final: ", "%.2f" % custo_final_1)

# Se o custo de fábrica for entr R$ 12.000,00 e R$ 25.000,00
if custo_consumidor > 12000.00 and custo_consumidor <= 25000.00:
    custo_final_2 = custo_consumidor * 1.25
    print("Custo Final: ", "%.2f" % custo_final_2)

# Se o custo de fábrica for superior a R$ 25.000,00
if custo_consumidor > 25000.00:
    custo_final_3 = custo_consumidor * 1.35
    print("Custo Final: ", "%.2f" % custo_final_3)
