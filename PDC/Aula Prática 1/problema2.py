#_*_coding: utf-8 _*_

velocidade = float(input('Digite o valor da velocidade: '))
# print(velocidade)

aceleracao = float(input('Digite o valor da aceleracao: '))
# print(aceleracao)

tempo = float(input('Digite o valor do tempo: '))
# print(tempo)

vfinal = velocidade + aceleracao * tempo
print("Velocidade final: ", "%.2f" % float(vfinal))

dist = velocidade * tempo + aceleracao * tempo ** 2 /2
print("Distância percorrida: ", "%.2f" % float(dist))