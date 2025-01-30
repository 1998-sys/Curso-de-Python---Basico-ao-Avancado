"""
Sets - conjuntos em Python (tipo set)

Representados graficamente pelo diagrama de Venn,
Sets em python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno

Parecem dicionários, mas não possuem chave, apenas valor.
"""

# set(iterável) ou {1,2,3} -> segundo caso é obrigatório passar os dados

# s1 = set()# Set vazio
# s1 = {'matheus', 1,2,3} # Set com valores
# print(s1, type(s1))

"""
Sets são eficientes para remover valores duplicados de iteráveis

- Não aceitam valores mutáveis
- Seus valores serão sempre únicos
- Não possuem índice
- Não garante a ordem dos elementos inseridos
- São iteráveis (for, in, not in )
"""
s2 = {1,2,3,3,1,3,3,3}
s3 = set('Matheus')
print(s2) # {1, 2, 3} -> valores únicos
print(s3) # {'M', 'a', 't', 'h', 'e', 'u', 's'} -> Não garante a ordem
#s4 = {['h']} -> TypeError: unhashable type: 'list' -> Não aceita valores mutáveis