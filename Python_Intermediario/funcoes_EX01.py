"""
Faça um programa para imprirmir

    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
"""

def convert_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print('A inserção informada não é numérica')


def imprime_tela (n):
    i=1
    while i <= n:
        print(f'{i}\t'*i)
        i += 1 


valor = convert_int('Informe o valor: ')

imprime_tela(valor)