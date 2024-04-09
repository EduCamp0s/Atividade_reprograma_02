import math

# Tamanho da área a ser pintada em metros quadrados
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Cobertura da tinta em metros quadrados por litro
cobertura_por_litro = 6

# Preços das latas e galões de tinta
preco_lata = 80
preco_galao = 25

# Cálculo da quantidade de tinta necessária com 10% de folga
quantidade_necessaria = area * 1.1 / cobertura_por_litro 

# Comprando apenas latas de 18 litros
quantidade_latas = math.ceil(quantidade_necessaria / 18)
preco_total_latas = quantidade_latas * preco_lata

# Comprando apenas galões de 3.6 litros
quantidade_galoes = math.ceil(quantidade_necessaria / 3.6)
preco_total_galoes = quantidade_galoes * preco_galao

# Misturando latas e galões
quantidade_latas_misturadas = math.floor(quantidade_necessaria / 18)
quantidade_galoes_misturados = math.ceil((quantidade_necessaria % 18) / 3.6)
preco_total_misturado = (quantidade_latas_misturadas * preco_lata) + (quantidade_galoes_misturados * preco_galao)

# Mostrando os resultados
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