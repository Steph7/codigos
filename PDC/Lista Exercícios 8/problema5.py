# _*_coding: utf-8 _*_

def nota_media_aluno(dicio, lista, nome):
    n = len(lista)
    soma = 0

    for aluno, notas in dicio.items():
        if nome is aluno:
            for materia, nota in notas.items():
                for materiaLista in lista:
                    if materia is materiaLista:
                        soma = soma + nota
    media = soma/n
    return media

