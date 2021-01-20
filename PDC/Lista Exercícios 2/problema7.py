# _*_coding: utf-8 _*_

salario = float(input())

prestacao_emprestimo = float(input())

valor_max = salario * 0.2

if(prestacao_emprestimo > valor_max):
    print('Empréstimo não concedido')

else:
    print('Empréstimo concedido')