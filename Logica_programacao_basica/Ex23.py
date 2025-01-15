# Faça um Programa que leia três números e mostre o maior deles

n1 = input('Informe o primeiro número: ')
n2 = input('Informe o segundo número: ')
n3 = input('Informe o terceiro número: ')

numeros = []

numeros.append(float(n1))
numeros.append(float(n2))
numeros.append(float(n3))

print(max(numeros))