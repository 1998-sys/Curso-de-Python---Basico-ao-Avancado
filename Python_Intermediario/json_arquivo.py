"""
A melhor estrutura para salvar um dicionário  python em um arquivo é Json
"""
import json

# pessoa = {
#     'nome':'Luiz Otávio Miranda',
#     'sobrenome': 'Miranda',
#     'enderecos':[
#         {'rua': 'R1', 'numero': 32},
#         {'rua':'R2', 'numero': 55},
#     ],
#     'altura':1.8,
#     'numeros_preferidos': (2,4,6,8,10),
#     'dev':True,
#     'nada': None
# }


# with open('json_arquivo.json', 'w', encoding='utf8') as arquivo:
#    json.dump(pessoa,
#             arquivo,
#             ensure_ascii=False, # formata os caracteres especiais
#             indent=2)  # Formata como dicionário
   


# Abrindo um arquivo json

with open('json_arquivo.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)



print(pessoa)