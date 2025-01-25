"""
Introdução às funções (def) em python
Funções são trechos de código usados para replicar determinada ação ao longo do seu código
Elas podem receber valores para parâmetros (agurmentos)
e retornar um valor específico
Por padrão, funções Python retornam None (Nada)
"""

def imprimir(a, b, c):
    print('Várias Vezes')


imprimir(1,2,3) # aqui são passados os parâmetros da função
imprimir(4,5,6) # Toda vez que eu chamar a função podemos mudar os parâmetros (código com valores diferentes)


def saudacao(nome = 'Sem nome'): # Setar o valor caso seja necessário
    print(f'Olá {nome}')

saudacao('Matheus')
saudacao('Maria')
saudacao()
