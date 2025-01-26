"""
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro.

"""

def converte(mensagem):

    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except:
            print('Informe um valor numérico !')


valor = converte('Informe o valor: ')

def operacao (valor):
    def multiplicacao (mult):
        return valor * mult
    return multiplicacao

multiplicar = operacao(valor)

for multiplicador in [2,3,4]:
    print(f'{multiplicar(multiplicador)}')


