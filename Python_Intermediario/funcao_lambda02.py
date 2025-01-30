"""
Converter as funções em funções lambda
"""
def executa(funcao, *args):
    return funcao(*args)



def soma(x,y):
    return x + y

#soma_l = lambda x,y : x+y # Má prática (por isso criar uma função específica para executar as lambdas)


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


print(
    executa (lambda x,y:x+y,
              [1,2,3,4,5],[6,7,8,9,10]
              )
)