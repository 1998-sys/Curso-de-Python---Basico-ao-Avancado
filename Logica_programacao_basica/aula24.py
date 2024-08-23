# Operadores in e not in
# Strings são iteráveis
# 0  1  2  3  4  5
# O  T  á  v  i  o
# -6-5-4-3-2-1

nome = 'Otávio'
# print(nome[2])

# # Está ?
# print('á' in nome)

# print('vio' in nome)

# print('m' not in nome)

# print('vio' not in nome) # Falso pois está na string 

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

print(1 or 0)