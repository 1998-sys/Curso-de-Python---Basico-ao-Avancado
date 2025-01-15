# Faça um Programa que leia três números e mostre-os em ordem decrescente

qtd = input('Informe a quantidade números que deseja incluir: ')
valores = []

for valor in range(int(qtd)):
    n = input(f'{valor + 1}º valor: ')
    valores.append(float(n))

valores.sort()

print(valores)