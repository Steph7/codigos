#_*_coding: utf-8 _*_

valor_reais = float(input('Digite um valor em reais: '))

cotacao_dolar_em_reais = float(input('Digite a cotação do dólar em reais de hoje: '))

valor_dolar = valor_reais / cotacao_dolar_em_reais
print("Valor em dólar: ", "%.2f" % valor_dolar)