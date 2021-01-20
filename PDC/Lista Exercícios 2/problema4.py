# _*_coding: utf-8 _*_

valor = int(input("Valor: "))
estado = input("Estado (sigla):")

if estado == 'MG':
    tx_imposto = 0.07
if estado == 'SP':
    tx_imposto = 0.12
if estado == 'RJ':
    tx_imposto = 0.15
if estado == 'MS':
    tx_imposto = 0.08

preco_final = valor * (1 + tx_imposto)
print("%.2f" % preco_final)