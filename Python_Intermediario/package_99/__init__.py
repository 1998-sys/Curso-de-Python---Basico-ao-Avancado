"""
Sempre que o pacote for importado esse será o primeiro módulo a ser executado
"""
print('Você importou o ', __name__)

def dobra(x):
    return x ** 2