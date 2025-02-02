"""
Dictionary Comprehension e Set Comprehension

"""

produto = {
    'nome': 'Caneta Azul',
    'preco':2.5,
    'categoria':'Escritório'
}


dc = {chave:valor.upper() if isinstance(valor,str) else valor for chave, valor in produto.items() if chave != 'categoria'}
print(dc)

# Comando isinstace pode receber mais de um parâmetro passando uma tupla ex: isinstance(variável, (int, float))

lista = [('a', 'Valor a'), ('b', 'Valor b'), ('c', 'Valor c')]

dc2 = {
    chave:valor for chave, valor in lista
}

print(dc2)


# também é possível converter pelo comando dict se tivermos uma estrutura com n tuplas (chave e valor)

dc3 = dict(lista)
print(dc3)

# Também é possível fazer com o set
set1 = {i for i in range(10)}
print(type(set1), set1)