"""
Métodos para string

split e join com list e str
split - Divide uma string
join - une uma string

"""

frase = 'Olha só que, coisa interessante'

# Split retorna uma lista com as divisões na string
lista_palavras = frase.split(',') # sem parâmetro quebra pelos espaços " ", mas também é possível passar o caracter de divisão
print(lista_palavras)

lista_frases_fixed = []
for i, frase in enumerate(lista_palavras):
     lista_frases_fixed.append(lista_palavras[i].strip()) # corta os espaços

print(lista_frases_fixed)


# Join - Unir uma string

frases_unidas = ' '.join(lista_frases_fixed)
print(frases_unidas)