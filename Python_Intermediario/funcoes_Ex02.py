"""
Faça um programa para imprimir:

    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
"""

def convert_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except:
            print('Informe um valor numérico')


def imprime(valor):
    i = 1
    for i in range(1,valor + 1):
        for j in range(1, i+1):
            print(f'{j}', end=" ")
        print()
        

valor = convert_int('Insira o valor: ')

imprime(valor)