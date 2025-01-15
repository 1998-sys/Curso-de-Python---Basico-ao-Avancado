"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

dias = {1: 'Domingo',
        2: 'Segunda',
        3: 'Terça-feira',
        4: 'Quarta-feira',
        5: 'Quinta-feira',
        6: 'Sexta-feira',
        7: 'Sábado'}

n = input('Informe um número que corresponte a um dia da semana: ')

if int(n) not in dias:
    print('Valor inválido')

else:
    print(f'{n} é correspondente a: {dias[int(n)]}')