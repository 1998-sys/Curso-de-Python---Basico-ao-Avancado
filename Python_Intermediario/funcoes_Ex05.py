
"""
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem
e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas
"""
import os


def convert_tipo(mensagem, tipo):
    """
    param mensagem: str -> Mensage of input
    param tipo: type -> Type of input
    return: type -> Return type of input
    """
    while True:
        try:
            return tipo(input(mensagem))
        except ValueError:
            print('Valor inválido. Tente novamente.')

def armazena_dados():
    """
    description: function to store data
    return: list -> Return list of data
    """
    dados = list()
    qtd_dados = convert_tipo('Informe a quantidade de dados a serem inseridas: ', int)
    for i in range(qtd_dados):
        taxa_imposto = convert_tipo(f'Digite a {i+1}° taxa de imposto: ', float)
        custo = convert_tipo(f'Informe a {i+1}° custo: ', float)
        dados.append((taxa_imposto, custo))
        os.system('cls')
    return dados



def soma_imposto(lista):
    """
    description: function to calculate the tax
    param lista: list -> List of data
    """
    for tupla in lista:
        taxa_imposto, custo = tupla # Desempacotamento da tupla 
        custo_com_imposto = custo + (custo * taxa_imposto)
        print(f'Custo original: {custo}, Custo com imposto: {custo_com_imposto}')



dados = armazena_dados()
soma_imposto(dados)