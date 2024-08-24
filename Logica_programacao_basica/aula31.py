"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade

"""

v1 = 'a'
v2 = 'b'

print(id(v1)) # identidade na memória
print(id(v2))

condicao = True
passou_no_if = None # Variável flag

if condicao:
    passou_no_if = True
    print('Faça Algo')
else:
    print('Não faça Algo')

print(passou_no_if, passou_no_if is not None)
print(passou_no_if, passou_no_if is None)

