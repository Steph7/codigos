# _*_coding: utf-8 _*_

def calcularTempo(salario_carlos, tx_poupanca, tx_rendafixa):
    salario_joao = salario_carlos * 1/3
    n = 0
    investimento_joao = salario_joao * ((1 + (tx_rendafixa/100)) ** n)
    investimento_carlos = salario_carlos * ((1 + (tx_poupanca/100)) ** n)
    
    while (investimento_joao <= investimento_carlos):
        investimento_joao = salario_joao * ((1 + (tx_rendafixa/100)) ** n)
        investimento_carlos = salario_carlos *((1 + (tx_poupanca/100)) ** n)
        n += 1
    n = n - 1 #Reajustando o período
    return n


salarioCarlos = float(input("Digite o salário do Carlos: "))
rendimentoPoupanca = float(input("Digite o rendimento da poupança(%): "))
rendimentoRendafixa = float(input("Digite o rendimento do fundo de renda fixa(%): "))

tempo = calcularTempo(salarioCarlos, rendimentoPoupanca, rendimentoRendafixa)

print("Meses: ", tempo)