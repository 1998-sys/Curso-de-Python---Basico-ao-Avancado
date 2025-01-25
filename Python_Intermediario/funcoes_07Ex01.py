"""
Exercícios com funções 

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável

Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.

"""

def converte(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except:
            print('informe um valor numérico !')

def mult(*args):
     total = 1
     for valor in args:
        total *= valor
     return total


i = 1
valores = list()
while i<=10:
    valor=converte(f'informe o {i}° valor: ')
    valores.append(valor)
    i+=1

multiplicacao = mult(*valores)
print(multiplicacao)
    




def par(numero):
    if numero %2 == 0:
        return (f'{numero} é par')
    return (f'{numero} é impar')
    
print(par(2))