# Concatenando e estendendo listas em python 

lista_a = [1,2,3]
lista_b = [4,5,6]

lista_c = lista_a + lista_b
print(lista_c)

lista_a.extend(lista_b) # Não retorna nada atua direto na lista a ser extendida
print(lista_a)