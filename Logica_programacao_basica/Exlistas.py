"""
Faça uma lista de compras com listas o usuário deve ter a possibilidade de inserir,
apagar e listar valores da sua lista. Não permita que o programa quebre com erros
de índices inexistentes na lista.

"""
from time import sleep
import os

valores = list()
opcao = ''

while True:
    opcao= input('Selecione a operação desejada:\n[I]nserir,[A]pagar,[L]istar,[S]air: ')[0].upper()
    if opcao == 'I':
        valores.append(input('Informe o valor: '))
        print('Inserindo valor..')
        sleep(2)
        print('Valor inserido !')
        sleep(1)
        os.system('cls')
    elif opcao == 'A':
        apagar = input('Informe um índice para apagar: ')
        try:
            indice = int(apagar)
            del valores[indice]
            print('Valor apagado...')
            print(valores)
            sleep(2)
            os.system('cls')
        except IndexError:
            print('o index não se encontra na lista !')
            continue
    elif opcao == 'L':
        if len(valores) == 0:
            print('Não há nada para listar')
        for i, valor in enumerate(valores):
            print(i, valor)
        sleep(3)
        os.system('cls')
    elif opcao == 'S':
        print('Saindo do programa...')
        sleep(2)
        break
    else:
        print('Selecione uma das operações citadas...')
        sleep(1)
        os.system('cls')
