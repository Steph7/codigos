#_*_coding: utf-8 _*_

montante = float(input('Digite o valor do investimento inicial: '))
# print(montante)

juros = float(input('Digite a taxa de juros: '))
# print(juros)

anos = float(input('Digite o período do investimento em anos: '))
# print(anos)

valorFinal = montante * (1 + (juros * 0.01)) ** anos
print("Valor Futuro: ", "%.2f" % valorFinal)