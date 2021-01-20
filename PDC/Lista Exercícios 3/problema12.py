# _*_coding: utf-8 _*_

def operacao(num1, num2, operador):
    if operador == '+':
        soma = num1 + num2
        return soma
    if operador == '*':
        mult = num1 * num2
        return mult
    if operador == '/':
        div = num1/num2
        return div

# Receber do usuário

numero1 = int(input())
numero2 = int(input())
simbolo = input()

x = operacao(numero1, numero2, simbolo)
print("%.2f" % x)