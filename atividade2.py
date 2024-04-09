import math


area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

cobertura_por_litro = 6

preco_lata = 80
preco_galao = 25

quantidade_necessaria = area * 1.1 / cobertura_por_litro 

quantidade_latas = math.ceil(quantidade_necessaria / 18)
preco_total_latas = quantidade_latas * preco_lata

quantidade_galoes = math.ceil(quantidade_necessaria / 3.6)
preco_total_galoes = quantidade_galoes * preco_galao

quantidade_latas_misturadas = math.floor(quantidade_necessaria / 18)
quantidade_galoes_misturados = math.ceil((quantidade_necessaria % 18) / 3.6)
preco_total_misturado = (quantidade_latas_misturadas * preco_lata) + (quantidade_galoes_misturados * preco_galao)

print("Quantidade de tinta necessária: {:.2f} litros".format(quantidade_necessaria))
print("\nOpção 1: Comprar {} latas de 18 litros, preço total: R$ {:.2f}".format(quantidade_latas, preco_total_latas))
print("Opção 2: Comprar {} galões de 3.6 litros, preço total: R$ {:.2f}".format(quantidade_galoes, preco_total_galoes))
print("Opção 3: Misturar {} latas e {} galões, preço total: R$ {:.2f}".format(quantidade_latas_misturadas, quantidade_galoes_misturados, preco_total_misturado))


if preco_total_latas <= preco_total_galoes and preco_total_latas <= preco_total_misturado:
    print("\nNossa empresa aconselha comprar:  Compre Latas\n")
elif preco_total_galoes <= preco_total_latas and preco_total_galoes <= preco_total_misturado:
    print("\nNossa empresa aconselha comprar: Compre Galões\n")
else:
    print("\nNossa empresa aconselha comprar: Misturar Latas e Galões\n")