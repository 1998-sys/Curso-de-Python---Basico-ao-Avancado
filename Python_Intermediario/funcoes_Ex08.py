

import os 
from time import sleep
from texttable import Texttable

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

def store(prestacao, dias_atraso): 
    """
        description: function to store data
        param prestacao: float -> Value of the installment
        param dias_atraso: int -> Value of the delay days
        return: list -> Return list of data
        """
    if not hasattr(store, "dados"):
            store.dados = list()
            
    store.dados.append((prestacao, dias_atraso))
    print('Dados armazenados com sucesso...')
    sleep(2)
    os.system('cls')
    return store.dados

def calculo(*args, multa=0.03, juros=0.01):
    """
    description: function to calculate the value of the installment
    param args: tuple -> Tuple of data
    param multa: float -> Value of the fine
    juros: float -> Value of the interest
    return: list -> Return list of calculated values
    """
    if not hasattr(calculo, "valores_calculados"):
        calculo.valores_calculados = list()
    else:
        calculo.valores_calculados.clear()
    
    for tupla in args:
        prestacao, dias_atraso = tupla    
        if dias_atraso > 0:
            valor = prestacao + (prestacao * multa) + (prestacao * dias_atraso * juros)
            calculo.valores_calculados.append(valor)
        elif dias_atraso == 0:
            calculo.valores_calculados.append(prestacao)
    return calculo.valores_calculados


def imprime_tabela(valores_calculados):
    """
    description: function to print the table
    param valores_calculados: list -> List of calculated values
    return: None
    """
    table = Texttable()
    table.add_row(['Prestações', 'Valor'])
    for i, valor in enumerate(valores_calculados, start=1):
        table.add_row([f'{i}° Prestação', f'R$ {valor:.2f}'])
    table.add_row(['Total', f'R$ {sum(valores_calculados):.2f}'])
    print(table.draw())



def main():

    prestacao = 1 
    dias_atraso = 0
    i = 1
    while prestacao > 0:
        prestacao = convert_tipo(f'Informe o valor da {i}° prestação: ', float)
        dias_atraso = convert_tipo('Informe a quantidade de dias de atraso: ', int)
        if prestacao > 0:
            dados = store(prestacao, dias_atraso)
        i += 1
        pagamentos = calculo(*dados)
        if prestacao <= 0:
            print('Programa encerrado...')
            sleep(2)
            os.system('cls')

    imprime_tabela(pagamentos)

    
   

if __name__ == "__main__":
    main()