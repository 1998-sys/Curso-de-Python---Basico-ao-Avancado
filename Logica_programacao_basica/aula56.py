"""
Faça uma lista de comprar com listas,
o usuário deve ter a possibilidade de inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
import os
from time import sleep
lista_compras = []
while True:
    acoes = [0,1,2,3]
    selecao = input('Selecione uma opção:\n'
                     '[0] - Sair\n[1] - incluir\n[2] - excluir\n[3] - listar\n')

    
    if len(selecao) > 1:
        print('A escolha deve ser apenas um digito, tente novamente....')
        sleep(2)
        os.system('cls')
        continue
    
    elif selecao.isdigit():
        if int(selecao) == 0:
            print('Finalizando Programa...')
            sleep(2)
            os.system('cls')
            break

        elif int(selecao) == 1:
            print('Inclusão de registro.....')
            valor = input('Insira o valor desejado: ')
            lista_compras.append(valor)
            print(f'{valor} inserido na lista !')
            sleep(3)
            os.system('cls')
        
        elif int(selecao) == 2:
            print('Exclusão de registro.....')
            indice = input('informe o indice para excluir: ')
            try:
                if indice.isdigit():
                    print(f'Removendo valor {lista_compras[int(indice)]}')
                    lista_compras.pop(int(indice))
                    sleep(2)
                    os.system('cls')
            except:
                print('Não foi possível apagar este índice')
                sleep(2)
                os.system('cls')
        
        elif int(selecao) == 3:
            print('Listando itens (index e valor)....')
            if lista_compras:

                for index,valor in enumerate(lista_compras):
                    print(index, valor)
                    sleep(1)
                
            else:
                print('Nada para Listar')
                sleep(2)
                os.system('cls')
    else:
        print('Entrada inválida, tente novamente')
        sleep(2)
        os.system('cls')
    