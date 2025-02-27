# groupby - agrupando valores (itertools)

from itertools import groupby

alunos = [
    {'nome':'Luiz', 'nota': 'A'},
    {'nome':'Leticia', 'nota': 'B'},
    {'nome':'Fabrício', 'nota': 'A'},
    {'nome':'Rosemary', 'nota': 'C'},
    {'nome':'Joana', 'nota': 'D'},
    {'nome':'João', 'nota': 'A'},
    {'nome':'Eduardo', 'nota': 'B'},
    {'nome':'André', 'nota': 'A'},
    {'nome':'Anderson', 'nota': 'C'},
]

# É necessário sempre ordenar para aplcar o groupby
alunos_agrupados = sorted(alunos, key=lambda a:a['nota'])
#print(alunos_agrupados)

#Aplicando groupby e passando a chave de agrupamento
grupos = groupby(alunos_agrupados, key=lambda a:a['nota'])

for chave, grupo in grupos:
    print(chave)
    print(list(grupo))

