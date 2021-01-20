# _*_coding: utf-8 _*_

def total_compra():
    x = 1
    print('Loja Quase Dois - Tabela de preços')
    while(x <= 50):
        total = 1.99 * x
        print(x, ' - R$ ', "%.2f" % total)
        x += 1
    exit()


total_compra()