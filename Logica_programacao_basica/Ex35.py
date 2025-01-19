"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16


"""

# valor = input('Informe o valor: ')

# if valor.isdigit():
    # print(f'{valor} é número')
    # inteiro = int(valor)
    # centenas = inteiro // 100
    # print(f'{centenas}')
    # dezenenas = (inteiro % 100) // 10
    # print(f'{dezenenas}')
    # unidade = inteiro % 10
    # print(unidade)
# else:
    # print(f'Valor não é número')


"""
Introdução ao try/except

try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

"""

numero_str = input('Vou dobrar o número que você digitar:')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_float} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')

try:
    print('STR: ', numero_str)
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')

except:
    print('Isso não é um número')