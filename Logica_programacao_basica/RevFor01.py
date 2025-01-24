"""
For - quando se tem o número de repetições
while - quando não se tem o número de repetições

"""

texto = 'Python'
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')
    