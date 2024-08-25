"""
quando temos a qtd de repetições a serem feitas utilizamos o for !
"""
 
texto = 'Python'

novo_texto= ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')