"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere "P", se seu argumento for positivo,
 e "N", se seu argumento for zero ou negativo.

"""

def verifica_valor(valor):
        return 'P' if valor > 0 else 'N'



valor = float(input('Informe um valor: '))

resultado = verifica_valor(valor)

print(resultado)