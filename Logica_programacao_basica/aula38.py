"""
Iterando strings com while
"""

nome = 'Matheus Bandeira' # Iteráveis
print(len(nome))
nova_string = ''
aux = 0
while aux < len(nome):
    nova_string += '*'+ nome[aux]
    aux +=1

nova_string += '*'
print(nova_string)

