import math

area = float(input("Digite aqui o tamanho da área a ser pintada em metros quadrados: "))

cobertura_por_litro = 3
litros_necessarios = math.ceil(area / cobertura_por_litro)
print("LITROS NECESSARIO DE TINTAS: ",litros_necessarios)

latas_por_litro = 18
cobertura_tinta = math.ceil(area / latas_por_litro)
print(cobertura_tinta)

informacoes_tintas = "As tintas são vendidas em latas de 18 litros que custam R$80,00."
print(informacoes_tintas)

valor_total = cobertura_tinta * 80
print("O valor total a pagar sera:R$", valor_total)









