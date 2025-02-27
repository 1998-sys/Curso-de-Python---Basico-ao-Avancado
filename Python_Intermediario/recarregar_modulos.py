"""
Por convenção o módulo só é importado uma vez para otimização de código, mas é possível faze o módulo ser carregado n vezes com importlib
"""
import importlib
import mudularizacao_m

print(mudularizacao_m.variavel_modulo)



# carregando n vezes o módulo

for i in range(10):
    importlib.reload(mudularizacao_m)
    print(f'for={i}')

print('Fim')