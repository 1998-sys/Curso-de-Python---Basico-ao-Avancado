"""
Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar

Funções decoradoras são funções que decoram outras funções,
decoradores são usados para fazer o python usar as funções decoradoras em outras funções
# Decoradores são "Syntax Sugar" (Açúcar sintático)
"""
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou decorar sua função')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print('Função decorada')
        return resultado
    return interna

@criar_funcao # decorador
def invert_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')


#inverte_string_checando_parametro = criar_funcao(invert_string)
#invertida = inverte_string_checando_parametro('123')
#print(invertida)

invertida = invert_string('123')
print(invertida)