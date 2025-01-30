"""
Métodos úteis dos dicionários em Python
- len -> Retorna o número de chaves do dicionário ou tamanho
- keys -> Retorna uma lista com as chaves do dicionário
- values -> Retorna uma lista com os valores do dicionário
- items -> Retorna uma lista de tuplas com chave e valor
- setdefault -> Retorna o valor da chave, se não existir, insere a chave com o valor (None por padrão)
- copy -> Retorna uma cópia do dicionário
- get -> Retorna o valor da chave, se não existir, retorna None
- pop -> Remove a chave específicada
- popitem -> Remove a última chave e valor
- update -> Atualiza o dicionário com outro dicionário ou com um iterável de tuplas

observação: se forem criadas chaves iguais no dicionário, a última chave criada será a que ficará no dicionário
"""

pessoa = {
    'Nome':'Matheus',
    'Sobrenome':'Bandeira' ,
    'Sobrenome':'Augusto'
}

#print(pessoa)

#print(len(pessoa))

# pode retornar tanto em dicionários como tupla
##rint(tuple(pessoa.values()))
#print(list(pessoa.items())) # Itens retorna ambos 

# Iterando pelo for
for c,v in pessoa.items():
    print(c,v)

pessoa.setdefault('idade', 26)
print(pessoa)

