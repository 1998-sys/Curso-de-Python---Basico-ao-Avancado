"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""
def converte_entradas(mensagem, tipo):
    while True:
        try:
            valor = tipo(input(mensagem))
            return valor
        except ValueError:
            print('Informe um valor numérico')

n1 = converte_entradas('informe o primeiro número inteiro: ', int)
n2 = converte_entradas('Informe o segundo número inteiro:' , int)


for i in range(n1,n2):
    print(i)
