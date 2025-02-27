"""
O primeiro módulo executado chama-se __main__ (primeiro arquivo a ser executado pelo python)
você pode importar outro módulo inteiro ou parte dele
O Python conhece a pasta onde o  __main__ está sendo executado e as pastas abaixo dele
Ele não reconhece pastas e módulos acima do __main__ por padrão
O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path
"""

print('Este módulo se chama', __name__)

#import mudularizacao_m # importando todo o módulo

from mudularizacao_m import variavel_modulo
print(variavel_modulo) # importando a variável do outro módulo
