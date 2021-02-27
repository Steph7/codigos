# _*_coding: utf-8 _*_

def definirMedias(aluno):
    dadosAlunos = aluno.split(" ")
    nome = dadosAlunos[0]
    notas = dadosAlunos[1:]
    soma = 0
    for x in notas:
        soma = soma + float(x)
    media = soma / len(notas)
    return media

f = open("notas.txt", "r")
texto = f.read()
alunos = texto.split("\n")

medias = []

for dados in alunos:
    medias.append(definirMedias(dados))

maior = None
menor = None

for media in medias:
    if(maior == None) or (media > maior):
        maior = media

for media in medias:
    if(menor == None) or (media < menor):
        menor = media

print(maior)
print(menor)
