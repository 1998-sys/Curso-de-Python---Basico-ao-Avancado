"""
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - limpa a lista
    extend - estente a lista
    + -  Concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10,20,30,40]
lista.append('Matheus')
print(lista)
nome = lista.pop() # Removeu o último item
lista.append(1233)
del lista [-1] # deletando pelo indíce
# lista.clear() - limpa a lista
lista.insert(0, 5) # adiciona o item e reordena 
print(lista)


