# Faça um Programa que peça dois números e imprima o maior deles.

n1 = input('Informe o primeiro número: ')
n2 = input('Informe o segundo número: ')

if float(n1) > float(n2):
    print(f'{n1} é o maior')
else:
    print(f'{n2} é o maior')