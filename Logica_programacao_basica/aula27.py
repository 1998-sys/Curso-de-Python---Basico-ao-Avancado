"""
Fatiamento de strings

012345678
Olá mundo
-987654321

Fatiamento [i:f:p][::]
Obs.: a função len retorna a qtd de caracteres
"""

variavel = 'Olá mundo'
print(variavel[5])
print(variavel[-4])

# Fatiamento (pegar uma fatia da string)
print(variavel[4:7]) # O índice final não é incluido

print(variavel[0:5])

# quantidade de caracteres
print(len(variavel))

# Passo (quantos em quantos caracteres vai pular)
print(variavel[0:len(variavel):2])

# passo invertido
print(variavel[-1:-10:-1])