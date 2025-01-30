p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

print(p1.get('cidade'), 'Não existe' ) # Retorna o valor da chave, caso não encontre None

# pop

#nome = p1.pop('nome') # Remove a chave e retorna o valor
#print(nome)
#print(p1)

# sobrenome = p1.popitem()
# print(sobrenome)
# print(p1)

# p1.update({
#     'nome':'João',
#     'idade': 26 # criando uma nova chave

# })



# outra forma de escrever o update
# p1.update(nome='Ezequiel', idade=18, estado = 'São Paulo', cidade = 'Campinas')
# print(p1)


# Outra forma com tuplas e também funciona com listas
tupla =(('profissão','DataScientist'), ('hob','Jogar bola'))  
p1.update(tupla)
print(p1)