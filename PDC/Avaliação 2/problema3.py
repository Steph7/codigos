# _*_coding: utf-8 _*_

def calculaIR(s_bruto):
    if(s_bruto <= 900.00):
        ir = 0
    elif(s_bruto > 900.00) and (s_bruto <= 1500.00):
        ir = s_bruto * (0.05)
    elif(s_bruto > 1500.00) and (s_bruto <= 2500.00):
        ir = s_bruto * (0.10)
    elif(s_bruto > 2500.00):
        ir = s_bruto * (0.20)
    return ir
        

valor_hora = float(input("Digite o valor da hora de trabalho: "))
quant_horas = int(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * quant_horas
print('Salário Bruto: R$', "%.2f" % salario_bruto)

imposto_renda = calculaIR(salario_bruto)
print('IR: R$', "%.2f" % imposto_renda)

inss = salario_bruto * 0.10
print('INSS: R$', "%.2f" % inss)

fgts = salario_bruto * 0.11
print('FGTS: R$', "%.2f" % fgts)

total_descontos = imposto_renda + inss
print('Total de descontos: R$', "%.2f" % total_descontos)

salario_liquido = salario_bruto - total_descontos
print('Salário líquido: R$', "%.2f" % salario_liquido)
