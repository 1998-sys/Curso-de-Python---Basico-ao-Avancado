"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

lista = []
print(lista)
print(type(lista))
print(bool(lista)) # Falsy

lista = [123, True, 'Luiz Otávio', 1.2, [1]]
print(lista)

# Acessando o itens da lista
print(lista[2].upper())
print(lista[-1])

# alterando itens da lista
lista[4] = 'Matheus'
print(lista)