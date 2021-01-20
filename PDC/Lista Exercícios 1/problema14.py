#_*_coding: utf-8 _*_

tempo = int(input('Digite o tempo em segundos: '))

segundos = tempo % 60

minutos = int((tempo / 60) % 60)

horas = int(tempo / 60 ** 2)

print(horas, minutos, segundos)