"""
enumerate - enumera iteráveis (índices), coloca os índices nos itens trazendo em uma tupla
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

#lista_enumerada = enumerate(lista)
# print(next(lista_enumerada))
# print(next(lista_enumerada))

for index, item in enumerate(lista, start=19): # tem como definir o start do enumerate
    print(index, item)