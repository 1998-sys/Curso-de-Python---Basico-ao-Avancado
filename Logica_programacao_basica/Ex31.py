"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

"""

from texttable import Texttable

def converte_num(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            return float(entrada)
        except ValueError:
            print('Entrada inválida! por favor insira um número correto')

l1 = converte_num('Informe o primeiro lado do triângulo: ')
l2 = converte_num('Informe o segundo lado do triângulo: ')
l3 = converte_num('Informe o terceiro lado do triângulo: ')



tabela = Texttable()

if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    if l1 == l2 and l2 == l3:
        mensagem = tabela.add_rows([['Mensagem', 'Classificação','Lado 1', 'Lado 2', 'Lado 3'],['É Triângulo', 'Equilátero', l1, l2, l3]])
    
    elif l1 == l2 or l2 == l3 or l3 == l1:
        mensagem = tabela.add_rows([['Mensagem', 'Classificação', 'lado 1', 'Lado 2','Lado 3'], ['É Triângulo !', 'Isóceles', l1,l2,l3]])
        
    else:
        mensagem = tabela.add_rows([['Mensagem', 'Classificação','lado 1','lado 2', 'lado 3'], ['É triângulo !', 'Escaleno',l1,l2,l3]])
    
else:
    mensagem = tabela.add_rows([['Mensagem', 'Classificação', 'lado 1', 'lado 2', 'lado 3'], ['Não é Triângulo !','NA', l1,l2,l3]])

print(mensagem.draw())