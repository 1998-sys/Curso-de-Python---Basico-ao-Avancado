"""
Faça um programa que leia 5 números e informe o maior número.
"""

def converte_float(mensagem, tipo):
    while True:
        try:
            valor = tipo(input(mensagem))
            return valor
        except ValueError:
            print(f'Valor não numérico informe novamente')

numeros = list()
i = 1

while i <= 5:
    v = converte_float(f'Informe o {i}° valor: ', float)
    numeros.append(v)
    i+=1


print(max(numeros))