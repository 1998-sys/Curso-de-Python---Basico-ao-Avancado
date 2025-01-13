# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []

for i in range (1,5):
    nota  = float(input(f'Informe a {i}° nota: '))
    notas.append(nota)

print(f'A média resultante é {sum(notas)/len(notas)}')