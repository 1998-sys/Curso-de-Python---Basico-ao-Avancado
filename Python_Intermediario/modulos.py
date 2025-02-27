"""
Módulos

(import, from, as e *)

- importar módulo inteiro: import nome_modulo
    - Vantagems: você tem o namespace do módulo
    - desvantagens: nomes grandes
se importar todo o módulo precisa utilizar o namespace.
"""

#import sys

#platform = 'A minha'
#print(sys.platform)
#print(platform)


"""
# partes = from nome_modulo import objeto1, objeto2
    - vantagens: nomes pequenos
    - desvantagems: sem o namespace do módulo, importa apenas os objetos desejados

"""
from sys import exit, platform

#exit()
print('blá')

"""
Alias 1 - criando apelido para o módulo
import nome_modulo as apelido
"""
import pandas as pd

"""
Alias 2 - apelidando objetos do módulo
from nome_modulo import objeto as apelido

"""

from sys import platform as pt

print(pt)