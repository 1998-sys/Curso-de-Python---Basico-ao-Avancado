"""
Generator expression, Iterables e iterator em Python 

Generator -> não tem tamanho nem ídice simplesmente faz uma iteração
"""
import sys

iterable = ['EU', 'Tenho', '__iter__']

# A responsabilidade do iterator é entregar o próximo valor
iterator = iter(iterable)   # tem __iter__ e __next__
print(iterator)
print(next(iterator))
lista = [n for n in range(10000)]
generator = (n for n in range(10000))
print(sys.getsizeof(generator)) # Generator não salva todos os valores na memória simplesmete entrega o valor (função que pausa)
print(sys.getsizeof(lista))

print(next(generator))
print(next(generator))

for n in generator:
    print(n)