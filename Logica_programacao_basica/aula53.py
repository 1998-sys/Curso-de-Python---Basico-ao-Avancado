"""
Introduçao ao desempacotamento + tuples (tuplas)
"""

nomes = ['Maria', 'Helena', 'Luiz']

nome1, nome2, nome3 = nomes

print(nome2)

# Resto dos valores *_ (esta variável está ali mas não será utilizada)
nome1, *_ = ["Matheus", 'Adilson', 'Luiz']

print(nome1)
print(*_)