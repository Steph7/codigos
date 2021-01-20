#_*_coding: utf-8 _*_

peso = float(input('Digite o peso (kg): '))
# print(peso)

altura = float(input('Digite a altura (m): '))
# print(altura)

imc = peso / altura ** 2
print("IMC: ", "%.2f" % imc)