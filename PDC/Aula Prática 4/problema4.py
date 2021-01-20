# _*_coding: utf-8 _*_

def tabela_paes(preco):
    x = 1
    while (x <= 50):
        total = x * preco
        print(x, ' - R$ ', "%.2f" % total)
        x += 1
    exit()

#RECEBER valor do produto do usuário

preco_pao = float(input("Digite o preço do pão: "))

tabela_paes(preco_pao)