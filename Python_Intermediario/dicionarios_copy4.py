"""
Métodos úteis dos dicionários em Python:
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
"""

d1 = {

    'c1':1,
    'c2':2,
}

d2 = d1 # cópia por referência

d2['c1'] = 1000 # A cópia rasa (Shallow copy) altera o valor nos dois dicionários pois o endereço na memória é o mesmo
print(d1)

d3 = d1.copy() # cópia por valor mudando o endereço na memória (Deep copy)

d3['c1'] = 1000000
print(d1)
print(d3)