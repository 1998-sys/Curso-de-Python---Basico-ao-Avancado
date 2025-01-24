"""
Altere o programa anterior para mostrar no final a soma dos números
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
l_num=list()

for i in range(n1,n2):
    l_num.append(i)

print(f'Soma = {sum(l_num)}')
