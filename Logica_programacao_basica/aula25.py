# Interpolação Básica de strings
#s - string
# d e i - int
# f - float
# x e X - hexadecimal (ABCDEF0123456789)

nome = 'Matheus'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)


# Utilizando hexadecimal
print('O hexadecimal de %d é %04X' % (1500,1500))