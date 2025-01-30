"""
List comprehension é uma forma rápida para criar listas a partir de iteráveis.

Sintaxe básica
[expr for item in lista]

"""
# lista = list()
# for numero in range(10):
#     lista.append(numero)

# print(lista)

lista_2 = [numero for numero in range(0,15)]
lista_3 = [numero **2 for numero in range(0,15)]
print(lista_2)
print(lista_3)