"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados

Se uma lista for maior que a outra a soma só vai considerar o tamanho da menor

"""

lista_a  = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]


def soma_listas (l1, l2):
    lista_agg = list(zip(l1,l2))
    lista_final = []
    for x, y in lista_agg:
        lista_final.append(x+y)
    return lista_final
        


print(soma_listas(lista_a, lista_b))

# outra forma 

lista_soma = [x+y for x,y in zip(lista_a, lista_b)]
print(lista_soma)