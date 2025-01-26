"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos

"""
from time import sleep


def convert_valores(mensagem, tipo=float):
    """
    Function to convert the input value to a specific type
    :param mensagem: str
    :param tipo: type (default float)
    :return: type   
    """
    while True:
        try:
            valor = tipo(input(mensagem))
            return valor
        except ValueError:
            print("Digite apenas números!")


def armazena_valores():
    """
    Function to store values in a list
    :return: list
    """
    valores = list()
    qtd_valores = convert_valores('Informe a quantidade de valores que deseja somar: ', int)
    print(type(qtd_valores))
    for valor in range(qtd_valores):
        valores.append(convert_valores(f'Informe o {valor+1}º valor: '))
    return valores


def soma_valores(*args):
    while True:
        opcao = input('Informe a operação desejada [S]omar ou  [P]arar:')[0].upper()
        if opcao == 'P':
            print('Programa finalizado!')
            sleep(2)    
            break
        elif opcao == 'S':
             return sum(args)
        else:
            print('Opção inválida!')


valores = armazena_valores()
print(f'A soma dos valores informados é: {soma_valores(*valores)}')