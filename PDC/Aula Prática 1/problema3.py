#_*_coding: utf-8 _*_

tempo = float(input('Digite o valor do tempo em segundos: '))
# print(tempo)

segundos = int(tempo % 60)

minutos = int((tempo / 60) % 60)

horas = int(tempo / 60 ** 2)

print("Valor convertido: ", horas, 'h', minutos, 'min', segundos, 's')