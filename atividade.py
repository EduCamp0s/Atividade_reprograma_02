# ATIVIDADE 16
#informar ao usuario a quatidade de latas de tinta a serem comprados e o preço total.
   #saber qual tamanho em metros da area a ser pintada
   

import math

#criar uma variavel com imput para saber o tamanho da area
area = float(input("Digite aqui o tamanho da área a ser pintada em metros quadrados: "))

# Definir cobertura de 1 litro de tinta em metros quadrados
cobertura_por_litro = 3
# Calcular os litros necessários de tinta
litros_necessarios = math.ceil(area / cobertura_por_litro)
print("LITROS NECESSARIO DE TINTAS: ",litros_necessarios)

#criar uma variavel para dividir o valor da area pela quantidade de latas por litro
latas_por_litro = 18
cobertura_tinta = math.ceil(area / latas_por_litro)
print(cobertura_tinta)

#criar variavel para informar o valor das tintas 
informacoes_tintas = "As tintas são vendidas em latas de 18 litros que custam R$80,00."
print(informacoes_tintas)

#criar variavel para multiplicar o valor de latas necessarias pelo valor de cada lata
valor_total = cobertura_tinta * 80
print("O valor total a pagar sera:R$", valor_total)









