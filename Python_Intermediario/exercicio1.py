"""
Exercícios

#Aumento os preços dos produtos a seguir em 10%
# Gere novos_novos produtos por deep copy (cópia profunda)

- Ordene os produts por nome descrecente (do maior para o menor)
Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

- Ordene os produtos por preço crescente (do menor para o maior)
Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""

produtos = [
    {'nome':'produto 5 ', 'preco': 10.00},
    {'nome':'produto 1', 'preco': 22.32},
    {'nome':'produto 3', 'preco': 10.11},
    {'nome':'produto 2', 'preco': 105.87},
    {'nome':'produto 4', 'preco': 69.90}
]


def aumenta_preco (lista):
    lista_profunda = lista.copy()
    for item in lista_profunda:
        item['preco'] = round(item['preco'] * 0.1 + item['preco'],2)
    return lista_profunda

def nome_descrescente(lista):
    lista_profunda = lista.copy()
    return sorted(lista_profunda, key = lambda item:item['nome'], reverse=True)

def preco_crescente(lista):
    lista_profunda = lista.copy()
    return sorted(lista_profunda, key = lambda item: item['preco'])






teste = aumenta_preco(produtos)
print(teste)

nome = nome_descrescente(teste)
print(nome)


teste3 = preco_crescente(nome)
print(teste3)