"""
Lista de listas e seus índices

"""

salas = [
    ['Maria', 'Helena'],
    ['Elaine',],
    ['Luiz', 'João','Eduarda', (0,10,20,30)]
]

print(salas)

for lista in salas: # primeiro for percorre a cada lista em sala
    for aluno in lista: # segundo for intera sobre o as listas de alunos
        print(aluno)


    
# Buscando pelo índice
# Helena
print(salas[0][1])