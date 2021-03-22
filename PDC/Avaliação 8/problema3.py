# _*_coding: utf-8 _*_

f = open("tempos.txt", "r")
texto = f.read()
linhas = texto.split("\n")

participantesCorrida = {}
menoresTempos = {}

for x in linhas:
    x = x.split()
    nome = x[0]
    tempos = x[::1]
    soma = 0
    menor = 0
    for tempo in tempos:
        if tempo not in nome:
            soma = soma + int(tempo)
            if (menor == 0) or (int(tempo) < menor):
                menor = int(tempo)
    media = soma/5
    participantesCorrida[nome] = media
    menoresTempos[nome] = menor


#print(menoresTempos)
menorTempo = sorted(menoresTempos, key = menoresTempos.get)
print("Melhor volta: %s - %d segundos" % (menorTempo[0], menoresTempos[menorTempo[0]]))



#print(participantesCorrida)
i = 1
print("Classificação Final: ")
for participante in sorted(participantesCorrida, key = participantesCorrida.get):
    print("%d - %s - %.2f" % (i, participante, participantesCorrida[participante]))
    i += 1
