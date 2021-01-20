# _*_coding: utf-8 _*_

def populacao(habitantesA, tx_crescimentoA, habitantesB, tx_crescimentoB):
    tempo = 0
    x = habitantesA * ((1 + tx_crescimentoA/100) ** tempo)
    y = habitantesB * ((1 + tx_crescimentoB/100) ** tempo)
    while (y >= x):
        x = habitantesA * ((1 + tx_crescimentoA/100) ** tempo)
        y = habitantesB * ((1 + tx_crescimentoB/100) ** tempo)
        tempo += 1
    print(tempo - 1)
    exit()


num_habitantesA = int(input("Digite a população da cidade A: "))
taxa_crescimentoA = float(input("Digite a taxa de crescimento da população da cidade A: "))
num_habitantesB = int(input("Digite a população da cidade B: "))
taxa_crescimentoB = float(input("Digite a taxa de crescimento da população da cidade B: "))

populacao(num_habitantesA, taxa_crescimentoA, num_habitantesB, taxa_crescimentoB)
