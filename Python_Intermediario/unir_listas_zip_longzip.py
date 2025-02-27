"""
Exercício - unir listas
Crie uma função zipper (como o zipper de roupas) o trabalho dessa função ser unir duas listas na ordem
Ex:

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

Resultado 
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

"""

from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(intervalo_maximo)
    ]


print(zipper(l1, l2))

# Função zip -> usa o valor da lista menor
print(list(zip(l1,l2)))

# Função zip_longest  -> usa o valor da lista maior
print(list(zip_longest(l1,l2)))