"""
Cuidados com dados mutáveis

= - Copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (Mutável)
"""

# Imutáveis
nome = 'Luiz'
noutra_variavel = nome
nome = 'joão'

print(nome)
print(noutra_variavel)

# Mutáveis

lista_a = ['Luiz' , 'Maria']
lista_b = lista_a

lista_a[0] = 'Qualquer coisa' #quando altera em uma altera nas duas
print(lista_b)

# Método retorna uma nova lista com outro endereçamento de memória 
lista_c = lista_a.copy()
lista_c[1] = 'outra coisa'

print(lista_a, lista_c)