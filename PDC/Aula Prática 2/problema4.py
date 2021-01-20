# _*_coding: utf-8 _*_

salario = float(input("Digite o valor do salário: "))

if salario >= 280:
    aumento = salario * 1.2
if salario > 280 and salario <= 700:
    aumento = salario * 1.15
if salario > 700 and salario <= 1500:
    aumento = salario * 1.1
if salario > 1500:
    aumento = salario * 1.05

valor_aumento = aumento - salario

print("Valor do aumento: ", "%.2f" % valor_aumento)
print("Novo salário: ", "%.2f" % aumento)