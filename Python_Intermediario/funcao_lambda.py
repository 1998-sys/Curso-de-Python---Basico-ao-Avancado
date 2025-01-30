"""
A função lambda é um função como qualquer outra em Python.
Porém, são funções anônimas que contém apenas uma linha. Ou seja, tudo
deve ser contido dentro de uma única expressão.

"""

# lista = [4,32,1,34,5,6,6,21] # Lista Original
# lista.sort() # Ordena a lista
# sorted(lista) # também ordena a lista.
# print(lista)

lista = [
    {'nome':'Matheus', 'Sobrenome':'Bandeira'},
    {'nome':'José', 'Sobrenome':'Bandeira'},
    {'nome':'Aline', 'Sobrenome':'Baldo'},
    {'nome':'Eliseu', 'Sobrenome':'Baldo'}
]

# def ordena(item): 
#     """
#     param item: str -> rece
#     """
#     return item['nome']

# lista.sort(key=ordena) # o próprio Python passa os valores da lista de forma automática.
# print(lista)


# Utilizando funções lambda
lista.sort(key= lambda item : item['nome'])
print(lista)