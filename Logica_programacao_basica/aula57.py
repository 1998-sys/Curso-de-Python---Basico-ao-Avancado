"""
Imprecisão de ponto flutuante
Double-Precision floating-point format IEEE 754

"""
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 5))


# utilizando o módulo decimal
import decimal

numero4 = decimal.Decimal(0.5)
print(numero4)