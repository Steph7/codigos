#_*_coding: utf-8 _*_

amigo_1 = float(input('Contribuição Amigo 1: '))
amigo_2 = float(input('Contribuição Amigo 2: '))
amigo_3 = float(input('Contribuição Amigo 3: '))
valor_premio = float(input('Valor do prêmio: '))

soma_contribuicoes = amigo_1 + amigo_2 + amigo_3

valor_recebido_a1 = valor_premio * amigo_1 / soma_contribuicoes
print("Valor recebido Amigo 1: ", "%.2f" % valor_recebido_a1)

valor_recebido_a2 = valor_premio * amigo_2 / soma_contribuicoes
print("Valor recebido Amigo 1: ", "%.2f" % valor_recebido_a2)

valor_recebido_a3 = valor_premio * amigo_3 / soma_contribuicoes
print("Valor recebido Amigo 1: ", "%.2f" % valor_recebido_a3)