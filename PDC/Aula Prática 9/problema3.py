# _*_coding: utf-8 _*_

alunoNotasmedia = dict()

while True:
    nome = input()
    nome = nome.strip()
    if not nome:
        break
    nota1 = float(input())
    nota2 = float(input())
    alunoNotasmedia[nome] = (nota1 + nota2) / 2

notas = []
for aluno, media in alunoNotasmedia.items():
    notas.append((media, aluno))
notas.sort(reverse = True)

for media, aluno in notas:
    print("%s - %.2f" % (aluno, media))