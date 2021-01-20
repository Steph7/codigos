# _*_coding: utf-8 _*_

def media(nota1, nota2, nota3, letra):
    # Calcular média aritmética
    if letra == 'A':
        soma = nota1 + nota2 + nota3
        media = soma/3
    if letra == 'P':
        peso1 = 5
        peso2 = 3
        peso3 = 2
        soma = (peso1 * nota1) + (peso2 * nota2) + (peso3 * nota3)
        media = soma/(peso1 + peso2 + peso3)
    return media


#Receber valores

prova1 = float(input())
prova2 = float(input())
prova3 = float(input())

# Se média aritmética: A
# Se média ponderada: P
tipo_media = input()

print("%.2f" % media(prova1, prova2, prova3, tipo_media))
