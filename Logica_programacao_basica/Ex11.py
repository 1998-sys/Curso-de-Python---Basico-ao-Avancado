"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo .
- a soma do triplo do primeiro com o terceiro.
- o terceiro elevado ao cubo.
"""

n1 = input('Informe o primeiro número inteiro: ')
n2 = input('Informe o segundo número inteiro: ')
n3 = input('Informe um número real: ')

print(f'O produto do dobro do primeiro com a metade do segundo é: {2*float(n1) * (float(n2)/2) }')
print(f'A soma do triplo do primeiro com o terceiro é: {(float(n1) * 3) + float(n3)}')
print(f'O terceiro elevado ao cubo é {pow(float(n3),3)}')