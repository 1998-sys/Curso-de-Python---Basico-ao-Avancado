"""
Higher Order Functions
Funções de primeira Classe
"""

def saudacao(msg):
    return msg

saudacao_2 = saudacao # é possível atribuir funções a determinada variável

v = saudacao('Bom dia')
print(v)

y = saudacao_2('Boa noite')
print(y)

# Também é possível utilizar funções "aninhadas" ou uma função executando a outra

def executa(funcao):
    return(funcao)

v2 = executa(saudacao_2)
print(v2)