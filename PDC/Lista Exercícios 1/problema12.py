#_*_coding: utf-8 _*_

preco_produto = float(input('Digite o valor do produto: '))

desconto_a_vista = preco_produto * 0.9
print("Preço com desconto à vista: ", "%.2f" % desconto_a_vista)

parcelado_6_x = preco_produto / 6
print("Preço de cada parcela (6X): ", "%.2f" % parcelado_6_x)

comissao_a_vista = desconto_a_vista * 0.05
print("Comissão vendedor venda à vista: ", "%.2f" % comissao_a_vista)

comissao_a_prazo = preco_produto * 0.05
print("Comissão vendedor venda à prazo: ", "%.2f" % comissao_a_prazo)