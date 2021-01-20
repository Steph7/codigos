# _*_coding: utf-8 _*_

def pagamento(valor_hora, quant_horas):
    #Definindo o valor do Salário Bruto
    salario = valor_hora * quant_horas

    print('Salário Bruto: ', "%.2f" % salario)

    if(salario <= 900):
        desconto_IR = salario * 0.00
    if(salario > 900 and salario <= 1500):
        desconto_IR = salario * 0.05
    if(salario > 1500 and salario <= 2500):
        desconto_IR = salario * 0.10
    if(salario > 2500):
        desconto_IR = salario * 0.20

    print("Desconto: ", "%.2f" %  desconto_IR)
    
    #Definindo o valor do Salário Líquido
    salario_liq = salario - desconto_IR

    print('Salário Líquido: ', "%.2f" % salario_liq)
    
    exit()

#INPUT usuário valor da horas trabalhadas 
v_hora = float(input("Digite o valor da hora trabalhada: "))
#INPUT usuário quantidade de horas trabalhadas 
q_hora = float(input("Digite a quantidade de horas trabalhadas: "))

pagamento(v_hora, q_hora)    
