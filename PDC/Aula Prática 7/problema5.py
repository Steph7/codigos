# _*_coding: utf-8 _*_

def definirMedias(aluno):
    dadosAlunos = aluno.split(" ")
    nome = dadosAlunos[0]
    notas = dadosAlunos[1:]
    soma = 0
    for x in notas:
        soma = soma + float(x)
    media = soma / len(notas)
    if(media >= 60):
        print("Nome: %s - Média: %.2f" % (nome, media))

f = open("notas.txt", "r")
texto = f.read()
alunos = texto.split("\n")

for dados in alunos:
    definirMedias(dados)
