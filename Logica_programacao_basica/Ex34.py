# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

from texttable import Texttable

def conversor_int(texto):
    while True:
        inteiro = input(texto)
        try:
            return int(inteiro)
        except ValueError:
            print('Entrada inválida, por favor informe um valor correto!')



tabela = Texttable()

print('Validador de datas formato dd/mm/aaaa'.upper().center(50))


meses = [1,3,5,7,8,10,12]

dia = conversor_int('Informe o dia: ')
mes = conversor_int('Informe o mês: ' )
ano = conversor_int('informe o ano: ')

if (0 < mes > 12) or  (0 < dia > 31) or ano < 1582:
    print(f'dia = {dia}, mês = {mes} ou ano = {ano} estão incorretos a data é inválida')
elif dia == 31 and mes in meses and ano >= 1582:  # Tratando o caso de 31 dias
    tabela.add_rows([['dia','mês','ano'],[dia,mes,ano]])
    print(tabela.draw())
if (0 < dia <= 30) and (1 <= mes <= 12) and ano >= 1582:
    tabela.add_rows([['dia','mês','ano'],[dia,mes,ano]])
    print(tabela.draw())