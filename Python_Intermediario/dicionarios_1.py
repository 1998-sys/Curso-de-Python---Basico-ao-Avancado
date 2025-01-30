"""
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo par de "chave" e "valor".
Chaves podem ser consideradas como "índice" que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos - {} - ou a classe dict para criar um dicionário.
Dados:
 - Imutáveis: int, float, str, tuple, bool
 - Mutáveis: list, dict, set

"""

pessoa = {
    'nome':'Matheus Bandeira',
    'sobrenome':'Miranda',
    'idade': 26,
    'altura': 1.80,
    'enderecos': [{'Rua':'x','numero':123},
                  {'Rua': 'b', 'bairro': 'y'}],
}

print(pessoa, type(pessoa))

# uma forma de acessar valores e chaves do dicionário
for c in pessoa:
    print(c, pessoa[c])