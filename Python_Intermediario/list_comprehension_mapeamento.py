"""
Mapeamento de dados em list comprehension - pega o dado e joga em outra lista com o mesmo tamanho e é possível fazer um operação

"""

produtos = [
    {'nome':'p1', 'preco':20},
    {'nome':'p2', 'preco':10},
    {'nome':'p3', 'preco':30},
]

novos_produtos = [{**produto, 'preco': produto['preco'] * 1.05} for produto in produtos if produto['preco'] > 10 ] # O If filtra
print(novos_produtos)