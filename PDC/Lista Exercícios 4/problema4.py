# _*_coding: utf-8 _*_

def menu():
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Saída')

    lista = [1, 2, 3, 4, 5]

    while True:
        opcao = int(input("Escolha uma opção: "))

        if opcao not in lista:
            print("Escolha um número válido! ")
        
        else:
            return opcao


while True:

    numero = menu()

    if numero == 5:
        exit()


    # Nº que serão operados
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))

    if numero == 1:
        operacao = num1 + num2
        print(operacao)

    elif numero == 2:
        operacao = num1 - num2
        print(operacao)
    
    elif numero == 3:
        operacao = num1 * num2
        print(operacao)
    
    elif numero == 4:
        operacao = num1 / num2
        print(operacao)

    