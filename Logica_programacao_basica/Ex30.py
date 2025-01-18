
"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

  O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

"""
from texttable import Texttable

n1 = input('Informe a primeira nota: ')
n2  = input('Informe a segunda nota: ')

media  = (float(n1) + float(n2))/2
tabela = Texttable()


if media > 9:
    tab = tabela.add_rows([['Média','Conceito','Mensagem'],[media, 'A', 'APROVADO']])
    
elif 7.5 < media < 9:
    tab = tabela.add_rows([['Média','Conceito', 'Mensagem'],[media, 'B', 'APROVADO']])

elif 6 < media <= 7.5:
    tab = tabela.add_rows([['Média', 'Conceito', 'Mensagem'], [media, 'C', 'APROVADO']])

elif 4 < media <= 6:
    tab = tabela.add_rows([['Média', 'Conceito', 'Mensagem'], [media, 'D', 'REPROVADO']])
else:
    tab = tabela.add_rows([['Média', 'Conceito', 'Mensagem'], [media, 'E', 'REPROVADO']])

print(tab.draw())
