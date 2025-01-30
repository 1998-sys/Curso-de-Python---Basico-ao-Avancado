"""
Métodos úteis para sets
- add() -> Adiciona um elemento ao set
- clear() -> Limpa o set
- discard() -> Remove um elemento do set, caso não encontre não retorna erro
- update() -> Atualiza o set com valores de outro iterável
"""

s1 = set()
s1.add(1)
s1.add('Matheus')
s1.update(('Boa noite', 5,4,3,52,1))
#s1.clear() lima o set
print(s1)

# Descartar o valor pelo próprio valor
s1.discard(1)

