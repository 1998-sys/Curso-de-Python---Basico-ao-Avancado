"""
Empacotamento e desempacotamento de dicionários

"""

# a,b= 1,2
# a,b = b,a
# print(a,b)

# pessoa = {
#     'nome': 'Aline',
#     'sobrenome': 'Baldo'
# }


# a,b = pessoa.items() # tupla com chave e valor

# print(a,b)

# for chave, valor in pessoa.items():
#     print(chave,valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Baldo'
}

dados_pessoa = {
    'idade':16,
    'altura':1.6
}

# para extrair os valores de um dicionário utilizamos **

pessoa_completa ={**pessoa, **dados_pessoa}
# print(pessoa_completa)

#args - retorna tupla
#kwargs - keyword arguments (argumentos nomeados ) -> retorna dicionário

def mostro_argumentos_nomeados(*args,**kwargs):
    print(f'não nomeados: {args}\n')

    print(kwargs)
    for chave, valor in kwargs.items():
        print(chave, valor)


#mostro_argumentos_nomeados(5,9,10,nome='Joana', qlq = 123)
mostro_argumentos_nomeados(pessoa_completa)