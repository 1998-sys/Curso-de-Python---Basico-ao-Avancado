"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e
fazer as consistências, informando ao usuário nas seguintes situações:

- Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
-Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
-Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
-Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

from texttable import Texttable
import math

tabela = Texttable()

def converte_num(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            return float(entrada)
        except ValueError:
            print('Entrada inválida ! por favor insira um número correto')


a = converte_num('Informe o valor do coeficiente A: ')
if a == 0:
    print('Programa encerrado a equação não é do segundo grau, valor de A=0')
    pass

else:
    b = converte_num('Informe o valor do coeficiente B: ')
    c = converte_num('Informe o valor do coeficiente C: ')  
    delta = pow(b,2) - 4*a*c
    if delta < 0:
        print(f'valor de delta = {delta} (negativo), a equação não possui raízes reais\n'
              'Encerrando o programa !')
    elif delta == 0:
        print(f'Valor de delta = {delta}, equação possui apenas uma raiz real !\n')
        x1 = -b/2*a
        tabela.add_rows([['RAIZ'], [x1]])
        print(tabela.draw())

    else:
        print(f'delta = {delta} equação possui duas raizes reais !\n')
        x1 = (-b + math.sqrt(delta))/2*a
        x2 = (-b - math.sqrt(delta))/2*a
        tabela.add_rows([['RAIZ 1', 'RAIZ 2'], [x1,x2]])
        print(tabela.draw())

